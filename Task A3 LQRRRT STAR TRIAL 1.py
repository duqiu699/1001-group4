import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.linalg import solve_continuous_are

class LQRRRTStarPlanner:
    def __init__(self, ox, oy, resolution, rr, step_size, boundary, Q, R, fc_x, fc_y, tc_x, tc_y):
        self.ox = ox
        self.oy = oy
        self.resolution = resolution
        self.rr = rr
        self.step_size = step_size
        self.boundary = boundary
        self.nodes = []
        self.Q = Q
        self.R = R
        self.fc_x = fc_x  # Fuel-cost area x-coordinates
        self.fc_y = fc_y  # Fuel-cost area y-coordinates
        self.tc_x = tc_x  # Time-cost area x-coordinates
        self.tc_y = tc_y  # Time-cost area y-coordinates

    class Node:
        def __init__(self, x, y, parent=None):
            self.x = x
            self.y = y
            self.parent = parent
            self.cost = float('inf')  # Cost-to-come

    def plan(self, sx, sy, gx, gy):
        """LQR-RRT* Planning"""
        start_node = self.Node(sx, sy)
        start_node.cost = 0  # Cost-to-come for the start node
        goal_node = self.Node(gx, gy)
        self.nodes.append(start_node)

        while True:  # Infinite loop until goal is found
            rnd_point = self.sample_point()
            nearest_node = self.get_nearest_node(rnd_point)
            new_node = self.lqr_steer(nearest_node, rnd_point)

            if self.is_collision_free(nearest_node, new_node):
                # Add new node with cost calculation
                new_node.cost = nearest_node.cost + self.distance(nearest_node, new_node)
                self.nodes.append(new_node)

                # Rewire nearby nodes
                neighbors = self.find_neighbors(new_node)
                best_parent = nearest_node
                best_cost = new_node.cost

                for neighbor in neighbors:
                    cost_to_neighbor = neighbor.cost + self.distance(neighbor, new_node)
                    if cost_to_neighbor < best_cost and self.is_collision_free(neighbor, new_node):
                        best_parent = neighbor
                        best_cost = cost_to_neighbor

                new_node.parent = best_parent
                new_node.cost = best_cost

                # Rewire other neighbors to potentially minimize their costs
                for neighbor in neighbors:
                    cost_through_new_node = new_node.cost + self.distance(new_node, neighbor)
                    if cost_through_new_node < neighbor.cost and self.is_collision_free(new_node, neighbor):
                        neighbor.parent = new_node
                        neighbor.cost = cost_through_new_node

                # Check if goal is reachable
                if self.distance(new_node, goal_node) <= self.step_size:
                    goal_node.parent = new_node
                    path = self.get_path(goal_node)
                    total_time = self.calculate_travel_time(path)
                    print(f"Total Travel Time: {total_time:.2f} minutes")
                    self.plot_path(path, sx, sy, gx, gy)
                    return path

    def sample_point(self):
        xmin, xmax, ymin, ymax = self.boundary
        x = random.uniform(xmin, xmax)
        y = random.uniform(ymin, ymax)
        return np.array([x, y])

    def get_nearest_node(self, point):
        return min(self.nodes, key=lambda node: self.distance(node, point))

    def lqr_steer(self, from_node, to_point):
        A = np.array([[0, 1], [0, 0]])  # State dynamics matrix
        B = np.array([[0], [1]])        # Input dynamics matrix
        P = solve_continuous_are(A, B, self.Q, self.R)
        K = np.linalg.inv(self.R) @ B.T @ P

        x_diff = np.array([to_point[0] - from_node.x, to_point[1] - from_node.y])
        u = -K @ x_diff
        dt = 0.1  # Time step
        new_x = from_node.x + x_diff[0] * dt + u[0] * dt ** 2 / 2
        new_y = from_node.y + x_diff[1] * dt + u[0] * dt ** 2 / 2

        return self.Node(new_x, new_y, from_node)

    def is_collision_free(self, from_node, to_node):
        xmin, xmax, ymin, ymax = self.boundary
        distance = self.distance(from_node, to_node)
        steps = max(1, int(distance / self.resolution))
        for i in range(steps + 1):
            x = from_node.x + i / steps * (to_node.x - from_node.x)
            y = from_node.y + i / steps * (to_node.y - from_node.y)
            if not (xmin <= x <= xmax and ymin <= y <= ymax):
                return False
            if not self.verify_node(x, y):
                return False
        return True

    def verify_node(self, x, y):
        for ox, oy in zip(self.ox, self.oy):
            if np.hypot(ox - x, oy - y) <= self.rr:
                return False
        return True

    def distance(self, p1, p2):
        if isinstance(p1, self.Node):
            p1 = np.array([p1.x, p1.y])
        if isinstance(p2, self.Node):
            p2 = np.array([p2.x, p2.y])
        return np.linalg.norm(p1 - p2)

    def get_path(self, goal_node):
        path = [(goal_node.x, goal_node.y)]
        node = goal_node
        while node.parent is not None:
            node = node.parent
            path.append((node.x, node.y))
        return path[::-1]

    def find_neighbors(self, new_node, gamma=30):
        """Find nearby nodes for rewiring"""
        n = len(self.nodes)
        dim = 2  # Assuming 2D space
        radius = gamma * (np.log(n) / n) ** (1 / dim)  # Dynamic search radius
        neighbors = []
        for node in self.nodes:
            if self.distance(new_node, node) <= radius:
                neighbors.append(node)
        return neighbors

    def calculate_travel_time(self, path):
        """
        Calculate travel time based on the geometry of the path.
        Adjust for fuel-cost and time-cost areas.
        """
        total_time = 0.0

        for i in range(1, len(path)):
            # Extract consecutive points from the path
            x1, y1 = path[i - 1]
            x2, y2 = path[i]

            # Calculate the Euclidean distance (segment length)
            segment_distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            time = segment_distance  # Base time is proportional to distance

            # Check if the segment's end point is in a cost-sensitive area
            if any(round(x2) == fx and round(y2) == fy for fx, fy in zip(self.fc_x, self.fc_y)):  # Fuel-cost area
                time *= 1.15  # Apply fuel cost multiplier
            elif any(round(x2) == tx and round(y2) == ty for tx, ty in zip(self.tc_x, self.tc_y)):  # Time-cost area
                time *= 1.3  # Apply time cost multiplier

            # Accumulate the time for this segment
            total_time += time

        return total_time



    def plot_path(self, path, sx, sy, gx, gy):
        """Highlight the final path"""
        plt.figure(figsize=(10, 10))

        # Plot barriers (obstacles)
        plt.plot(self.ox, self.oy, ".k", label="Obstacles")

        # Plot cost-sensitive areas
        plt.scatter(self.fc_x, self.fc_y, c="yellow", s=10, alpha=0.5, label="Fuel-Cost Area")
        plt.scatter(self.tc_x, self.tc_y, c="red", s=10, alpha=0.5, label="Time-Cost Area")

        # Plot all iteration paths (tree)
        for node in self.nodes:
            if node.parent:
                plt.plot([node.x, node.parent.x], [node.y, node.parent.y], "-g", alpha=0.5)

        # Plot start and goal
        plt.plot(sx, sy, "ro", markersize=10, label="Start")
        plt.plot(gx, gy, "bo", markersize=10, label="Goal")

        # Plot the final path
        for i in range(len(path) - 1):
            plt.plot([path[i][0], path[i + 1][0]], [path[i][1], path[i + 1][1]], "-r", linewidth=2, label="Path" if i == 0 else "")

        plt.legend()
        plt.grid(True)
        plt.axis("equal")
        plt.show()
# Aircraft data from the table
aircraft_data = {
    "A321neo": {
        "fuel_rate": 54,  # kg/min
        "passenger_capacity": 200,
        "time_cost": {"low": 10, "medium": 15, "high": 20},  # $/min
        "fixed_cost": 1800  # $
    },
    "A330-900neo": {
        "fuel_rate": 84,  # kg/min
        "passenger_capacity": 300,
        "time_cost": {"low": 15, "medium": 21, "high": 27},  # $/min
        "fixed_cost": 2000  # $
    },
    "A350-900": {
        "fuel_rate": 90,  # kg/min
        "passenger_capacity": 350,
        "time_cost": {"low": 20, "medium": 27, "high": 34},  # $/min
        "fixed_cost": 2500  # $
    },
}

# Scenario data
scenarios = [
    {
        "name": "Scenario 1",
        "passengers": 3000,
        "max_flights": 12,
        "time_cost_level": "medium",
        "fuel_cost": 0.76  # $/kg
    },
    {
        "name": "Scenario 2",
        "passengers": 1250,
        "max_flights": 5,
        "time_cost_level": "high",
        "fuel_cost": 0.88  # $/kg
    },
    {
        "name": "Scenario 3",
        "passengers": 2500,
        "max_flights": 25,
        "time_cost_level": "low",
        "fuel_cost": 0.95  # $/kg
    },
]

# Function to calculate cost for one aircraft
def calculate_cost(aircraft, scenario, total_travel_time):
    fuel_rate = aircraft["fuel_rate"]  # kg/min
    passenger_capacity = aircraft["passenger_capacity"]
    time_cost = aircraft["time_cost"][scenario["time_cost_level"]]
    fixed_cost = aircraft["fixed_cost"]

    # Calculate fuel cost
    trip_fuel = fuel_rate * total_travel_time  # kg
    fuel_cost = trip_fuel * scenario["fuel_cost"]

    # Calculate time cost
    time_cost_total = time_cost * total_travel_time

    # Total cost for one flight
    cost_per_flight = fuel_cost + time_cost_total + fixed_cost

    # Calculate number of flights needed
    flights_needed = -(-scenario["passengers"] // passenger_capacity)  # Ceiling division

    # Ensure flights do not exceed the maximum allowed
    if flights_needed > scenario["max_flights"]:
        return "Inapplicable"  # Mark as inapplicable if flights exceed the max

    # Total cost for the aircraft
    total_cost = flights_needed * cost_per_flight
    return total_cost

# Main function to determine the best aircraft for each scenario
def find_best_aircraft_for_scenarios(scenarios, aircraft_data, total_travel_time):
    for scenario in scenarios:
        print(f"\nEvaluating {scenario['name']}...")
        best_aircraft = None
        lowest_cost = float("inf")

        # Store costs or inapplicability for all aircraft
        aircraft_costs = {}

        for aircraft_name, aircraft in aircraft_data.items():
            cost = calculate_cost(aircraft, scenario, total_travel_time)
            aircraft_costs[aircraft_name] = cost
            if cost != "Inapplicable" and cost < lowest_cost:
                lowest_cost = cost
                best_aircraft = aircraft_name

        # Output costs for all aircraft
        for aircraft_name, cost in aircraft_costs.items():
            if cost == "Inapplicable":
                print(f"{aircraft_name}: Inapplicable (exceeds maximum flights)")
            else:
                print(f"{aircraft_name}: Total Cost = ${cost:.2f}")

        # Output the best aircraft
        if best_aircraft:
            print(f"Best Aircraft: {best_aircraft} with Total Cost: ${lowest_cost:.2f}")
        else:
            print("No applicable aircraft for this scenario.")



def main():
    ox, oy = [], []

    # Define obstacles
    for i in range(-10, 60, 1):
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60, 1):
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60, 1):
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60, 1):
        ox.append(-10.0)
        oy.append(i)

    # Slanting obstacles
    for i in range(0, 60, 1):
        ox.append((i - 30) / -3)
        oy.append(i)
    for i in range(-10, 30, 1):
        ox.append(i)
        oy.append(-15 / 40 * i + 90 / 8 + 45)
    for i in range(10, 50, 1):
        ox.append(i)
        oy.append(-1 / 4 * i + 32.5)

    # Define cost-sensitive areas
    fc_x, fc_y = [], []
    for i in range(25, 30, 1):
        for j in range(0, 20, 1):
            fc_x.append(i)
            fc_y.append(j)

    tc_x, tc_y = [], []
    for i in range(35, 50, 1):
        for j in range(35, 50, 1):
            tc_x.append(i)
            tc_y.append(j)

    boundary = (-10, 60, -10, 60)
    sx, sy = -5, 20  # Start
    gx, gy = 40, 55  # Goal
    resolution = 1.0
    robot_radius = 1.0
    step_size = 3.0
    Q = np.diag([1.0, 0.1])
    R = np.diag([0.01])

    lqr_rrt_star = LQRRRTStarPlanner(ox, oy, resolution, robot_radius, step_size, boundary, Q, R, fc_x, fc_y, tc_x, tc_y)
    
    print("\nCalculating the best aircraft based on the travel time...")
    try:
        path = lqr_rrt_star.plan(sx, sy, gx, gy)
        total_travel_time = lqr_rrt_star.calculate_travel_time(path)
        find_best_aircraft_for_scenarios(scenarios, aircraft_data, total_travel_time)
    except Exception as e:
        print(f"An error occurred during pathfinding or cost calculation: {e}")


if __name__ == "__main__":
    main()


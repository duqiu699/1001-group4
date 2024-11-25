"""
GBFS
author: Ilshat25
"""
import math
import matplotlib.pyplot as plt

show_animation = True


class GreedyBestFirstSearch:
    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y):
        self.resolution = resolution
        self.rr = rr
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model()
        self.calc_obstacle_map(ox, oy)

        self.fc_x = fc_x
        self.fc_y = fc_y
        self.tc_x = tc_x
        self.tc_y = tc_y

        self.time_cost_multiplier = 1.3  # 30% additional cost in time-cost area
        self.fuel_cost_multiplier = 1.15  # 15% additional cost in fuel-cost area

    class Node:
        def __init__(self, x, y, cost, parent_index):
            self.x = x
            self.y = y
            self.cost = cost
            self.parent_index = parent_index

    def planning(self, sx, sy, gx, gy):
        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_grid_index(start_node)] = start_node
        path_found = False

        while open_set:
            current_id = min(
                open_set, key=lambda o: self.calc_heuristic(goal_node, open_set[o]))
            current = open_set[current_id]

            if current.x == goal_node.x and current.y == goal_node.y:
                print("Goal reached!")
                goal_node.parent_index = current.parent_index
                path_found = True
                break

            del open_set[current_id]
            closed_set[current_id] = current

            for motion in self.motion:
                node = self.Node(current.x + motion[0],
                                 current.y + motion[1],
                                 current.cost, current_id)

                if not self.verify_node(node) or self.calc_grid_index(node) in closed_set:
                    continue

                # Adjust cost based on location
                grid_x = self.calc_grid_position(node.x, self.min_x)
                grid_y = self.calc_grid_position(node.y, self.min_y)

                if round(grid_x) in self.tc_x and round(grid_y) in self.tc_y:
                    node.cost += self.time_cost_multiplier
                elif round(grid_x) in self.fc_x and round(grid_y) in self.fc_y:
                    node.cost += self.fuel_cost_multiplier

                # Add to open set
                open_set[self.calc_grid_index(node)] = node

        if not path_found:
            print("Path not found.")
            return [], []

        return self.calc_final_path(goal_node, closed_set)

    def calc_final_path(self, goal_node, closed_set):
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)]
        parent_index = goal_node.parent_index
        while parent_index != -1:
            node = closed_set[parent_index]
            rx.append(self.calc_grid_position(node.x, self.min_x))
            ry.append(self.calc_grid_position(node.y, self.min_y))
            parent_index = node.parent_index
        return rx, ry

    def calc_heuristic(self, n1, n2):
        return math.hypot(n1.x - n2.x, n1.y - n2.y)

    def calc_grid_position(self, index, min_position):
        return index * self.resolution + min_position

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x or py < self.min_y or px >= self.max_x or py >= self.max_y:
            return False
        if self.obstacle_map[node.x][node.y]:
            return False
        return True

    def calc_obstacle_map(self, ox, oy):
        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)

        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)]
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy):
                    if math.hypot(iox - x, ioy - y) <= self.rr:
                        self.obstacle_map[ix][iy] = True
                        break

    @staticmethod
    def get_motion_model():
        return [[1, 0], [0, 1], [-1, 0], [0, -1],
                [-1, -1], [-1, 1], [1, -1], [1, 1]]


def calculate_total_time(rx, ry, tc_x, tc_y, fc_x, fc_y):
    total_time = 0
    for i in range(1, len(rx)):
        x1, y1 = rx[i - 1], ry[i - 1]
        x2, y2 = rx[i], ry[i]
        distance = math.hypot(x2 - x1, y2 - y1)

        # Adjust time for time-cost area
        if round(x1) in tc_x and round(y1) in tc_y:
            distance *= 1.3  # Increase by 30%

        # Adjust time for fuel-cost area
        elif round(x1) in fc_x and round(y1) in fc_y:
            distance *= 1.15  # Increase by 15%

        total_time += distance

    return total_time


def main():
    sx, sy = -5.0, 20.0
    gx, gy = 40.0, 55.0
    grid_size = 1.0
    robot_radius = 1.0

    ox, oy = [], []
    for i in range(-10, 60):
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60):
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60):
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60):
        ox.append(-10.0)
        oy.append(i)

    for i in range(0, 60):
        ox.append((i - 30) / -3)
        oy.append(i)

    for i in range(-10, 30):
        ox.append(i)
        oy.append(-15 / 40 * i + 90 / 8 + 45)

    for i in range(10, 50):
        ox.append(i)
        oy.append(-1 / 4 * i + 32.5)

    tc_x, tc_y = [], []
    for i in range(35, 50):
        for j in range(35, 50):
            tc_x.append(i)
            tc_y.append(j)

    fc_x, fc_y = [], []
    for i in range(25, 30):
        for j in range(0, 20):
            fc_x.append(i)
            fc_y.append(j)

    gbfs = GreedyBestFirstSearch(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = gbfs.planning(sx, sy, gx, gy)

    # Calculate the total travel time
    total_time = calculate_total_time(rx, ry, tc_x, tc_y, fc_x, fc_y)
    print(f"Total Travel Time: {total_time:.2f} minutes")

    # Perform cost evaluation for scenarios
    find_best_aircraft_for_scenarios(scenarios, aircraft_data, total_time)

    if show_animation:
        plt.plot(ox, oy, ".k", label="Obstacles")
        plt.plot(tc_x, tc_y, "or", label="Time-Cost Area")
        plt.plot(fc_x, fc_y, "oy", label="Fuel-Cost Area")
        plt.plot(sx, sy, "og", label="Start")
        plt.plot(gx, gy, "xb", label="Goal")
        plt.plot(rx, ry, "-r", label="Path")
        plt.legend()
        plt.grid(True)
        plt.axis("equal")
        plt.show()


# Aircraft data from the LQR RRT* code
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

# Scenario data from the LQR RRT* code
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

# Cost calculation function (reused from LQR RRT*)
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


if __name__ == "__main__":
    main()


<p align="center">
 <h2 align="center">1001-group4</h2>
 
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block;">Table of Contents</h2></summary>
  <ul>
    <li><a href="#Introduction">Introduction</a></li>
    <li><a href="#task-1">Task 1</a></li>
    <li><a href="#task-2">Task 2</a></li>
    <li><a href="#task-3">Task 3</a></li>
    <li><a href="#task-A1">Task A1</a></li>
    <li><a href="#task-A2">Task A2</a></li>
    <li><a href="#task-A3">Task A3</a></li>
    <li><a href="#Reflections">Reflections</a></li>
    <li><a href="#contacts">Contacts</a></li>
  </ul>
</details>

# Introduction
 For airlines, the most important thing is profitability. Therefore, they are committed to using various methods to enhance the benefits of their routes. This project aims to identify corresponding methods that can improve route profitability through different tasks.
 
## Task 1

In the following task, we will find an approciate aircraft model that achieve minimum cost for each scenario for the challenge assigned to our group.

First of all, we are going to find the shortest route from the departure point to arrival point in our group's obstacle set, then determine the aircraft type for each scenario to achieve minimum cost while satisfying passenger needs.

The aircraft type we have:
1. A321neo
2. A330-900neo
3. A350-900

First, the obstacle set for our group:
![IMAGE ALT TEXT HERE](https://i.postimg.cc/Hx1CWHPS/obstacle1.png)


By editing the python programme, we can find the shortest way:
![IMAGE ALT TEXT HERE](https://i.postimg.cc/kXpzXq2x/image.png)


To find the minimum cost, we have to use to following formula:
![IMAGE ALT TEXT HERE](https://i.postimg.cc/0QnHgsgK/image.png)

 The 3 scenario:

1.  Scenario 1:
    - 3000 passengers travel within 1 week.
    - 12 flights maximum for one week
    - Time cost= Medium and Fuel Cost= 0.76 $/kg.

2.  Scenario 2:
    - 1250 passengers travel within 1 month.
    - 5 flights maximum for one week
    - Time cost= High and Fuel Cost= 0.88 $/kg.

3.  Scenario 3:
    - 2500 passengers travel within 1 week.
    - 25 flights maximum for one week
    - Time cost= low and Fuel Cost= 0.95 $/kg.
  
### Coding
[1code](https://github.com/duqiu699/1001-group4/blob/main/final%20code%20of%20task%201)
### Conclusion:
 * For scenario 1,the aircraft with the lowest operation cost is <ins></ins>, it can conduct the amount of flight is <ins></ins>.
 * For scenario 2,the aircraft with the lowest operation cost is <ins></ins>, it can conduct the amount of flight is <ins></ins>.
 * For scenario 3,the aircraft with the lowest operation cost is <ins></ins>, it can conduct the amount of flight is <ins></ins>.


## Task 2

  In the following task, we are going to design a new cost area that can reduce the cost of the route.

  ### Jetstream
   A jet stream is a fast-flowing, narrow air current found in the atmosphere of some planets, including Earth. On Earth, jet streams are located near the altitude of the tropopause and are westerly winds (flowing west to east). Their paths typically have a meandering shape and can be thousands of kilometers long, a few hundred kilometers wide, and a few kilometers deep.
   ![IMAGE ALT TEXT HERE](https://i.postimg.cc/FRGmT8DD/image.png)
  https://svs.gsfc.nasa.gov/3864

  ### Background

  By using the same obstacle set and scenario 1 in task 1, we are going to find the best place to set our minus-cost-area(jetstream) for this test, while the cost in jetstream area can be reduced by 5%. The area of jetstream will span across the map laterally and span 5-unit length vertically.
  

  By editing programme, we can find the best place of Jetstream:
    ![IMAGE ALT TEXT HERE](https://i.postimg.cc/G2MwFYmf/image.png)

    
  ### Conclusion
  After completing this task, we can recognize the importance of jet streams in the aviation industry, especially in terms of fuel savings and reducing flight times. At the same time, it has deepened our understanding and use of Python programming.
## Task 3
  In the following task, we are going to design a new aircraft by finding out its parameters based on the restrictions.

  ### Situation
   - Aircraft should be fit Scenario 1 in task 1.
   - Only consider cruise time.
   - Passenger capacity.(min 100 to max 450)
   - Each 50 passenger increase time cost by $2/min.(Base with $12)
   - Base with Twin-engine aircraft, if capacity>=300, must use 4-engine aircraft.
   - Fixed cost is 2000 for Twin-engine aircraft, 2500 for 4-engine aircraft.
   - Each engine consumes fuel at 20kg/min.

  ### Our calculation
  
## Task A1
  In the following task, the aircraft will be a supply craft that must reach 2 drop-off points to drop supplies before heading to base.
  ### Situation
  - One checkpoint should be added in cost intensive area
  - All checkpoint need to be reached before arriving at the destination.

## Task A2
  In the following task, the mission and the environment keep changing for each environment.
  ### Situation
   - The fuel-consuming area (fixed 40x40) remains and generate it randomly.
   - No diagonal movement, change parameter and object travel within one grid size.
   - Generate obstacles randomly with reasonable density.
   - Starting and Ending point are generated randomly (>= 40-unit in between)
   - Fuel-consuming area won't cover the obstacles and no obstacles should be generate at/near start and end point.

## Task A3

## Reflection

  ### Lee Ching (24028115D)
  
  ### Song Yujie (24103111D)
  
  ### Kao Ching Yiu (24083458D)
  
  ### Ng Chi Hin (24083458D)

## Table of content

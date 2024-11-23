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
![](https://i.postimg.cc/Hx1CWHPS/obstacle1.png)


By editing the python programme, we can find the shortest way:
![](https://i.postimg.cc/kXpzXq2x/image.png)


To find the minimum cost, we have to use to following formula:
![](https://i.postimg.cc/0QnHgsgK/image.png)

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
  
### Manuel Calculation
![](https://i.postimg.cc/T2ZYdypk/IMG-2060.jpg)
  
### Coding
[1code](https://github.com/duqiu699/1001-group4/blob/main/final%20code%20of%20task%201)

#### Firstly, set initial condition(start and goal position; border; cost intensive area)
![](https://i.postimg.cc/8CFqxCGz/temp-Image6-CO4-El.avif)
![](https://i.postimg.cc/Zq11mhYF/temp-Imagee-GJYSE.avif)
![IMAGE ALT TEXT HERE](https://i.postimg.cc/G2G6hSH0/temp-Imageg-Rb-TK0.avif)

#### Secondly, calculate trip cost
##### ---input all data of three scenarios and use dictionary to encapsulate data of three types of aircrafts.
![IMAGE ALT TEXT HERE](https://i.postimg.cc/25wz86JF/temp-Image-NT4-Ib-E.avif)

##### ---calculate the total cost if the flights number is eligible.
![IMAGE ALT TEXT HERE](https://i.postimg.cc/yNYNRc0r/temp-Image-Gl-Rf66.avif)

### Conclusion:
 * For scenario 1,the aircraft with the lowest operation cost is <ins>A330-900neo</ins>, it can conduct the amount of flight is <ins>$109128</ins>.
 * For scenario 2,the aircraft with the lowest operation cost is <ins>A350-900</ins>, it can conduct the amount of flight is <ins>$57568</ins>.
 * For scenario 3,the aircraft with the lowest operation cost is <ins>A321neo</ins>, it can conduct the amount of flight is <ins>$107117</ins>.


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

  ### Coding
  #### Firstly，add a third code to modify the cost
  ![IMAGE ALT TEXT HERE](https://i.postimg.cc/GpQ7XQYT/temp-Image1-TTOAy.avif) 
  
  #### Secondly, add less cost in jet stream by mimicing the code of cost intensive area
  ![IMAGE ALT TEXT HERE](https://i.postimg.cc/PNsQXpYk/temp-Imagevmv-Ysq.avif)
  
  #### Thirdly, set cost reduced area 3.
  We can change the number in the second line of code to change the position of jet stream.
  ![IMAGE ALT TEXT HERE](https://i.postimg.cc/jSCPp4GJ/temp-Image-Yr-BWxe.avif)
  
  #### Lastly, plot the cost reduced area 3
  ![IMAGE ALT TEXT HERE](https://i.postimg.cc/k4w5MkSM/temp-Imagenf-Sy-XK.avif)
  
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
  ![imade](https://i.postimg.cc/fyJxKmKG/20241112002252.jpg)
  the airbus program
  ![image](https://i.postimg.cc/tRN7g237/2024-11-12-122418.png)
## Task A1
  In the following task, the aircraft will be a supply craft that must reach 2 drop-off points to drop supplies before heading to base.
  ### Situation
  - One checkpoint should be added in cost intensive area
  - All checkpoint need to be reached before arriving at the destination.

  ### Coding
  #### Firstly, add one checkpoint for each cost intensive area
  <ins>cp1x</ins> and <ins>cp1y</ins> are for checkpoint1, <ins>cp2x</ins> and <ins>cp2y</ins> are for checkpoint2
  we can also adjust the checkpoint by change the number
  ![](https://i.postimg.cc/rpq32J6c/temp-Imagew-Hs-J3-C.avif)

  #### Secondly, reach all checkpoints before arriving at the destination
  Because of the aircraft need to each all checkpoints before arriving at the destination, we can divide the path into three parts, calculate the time spent on each part and add it together to get the total time.
  ![](https://i.postimg.cc/ZY6Qn2TZ/temp-Image-Fx-Arqa.avif)

  ### Conclusion
  The finally path and output are in the following pictures.
  the checkpoints shows before the path display
  ![](https://i.postimg.cc/4NBBhTjC/temp-Image-Dr-Jw-Om.avif)
  ![](https://i.postimg.cc/vHB5kx2j/temp-Image-Jk6b-M4.avif)
  Comment: The correct path can be displayed, but there are two unrelated lines, which is a problem with the code that we can't solve for the moment.
  

## Task A2
  In the following task, the mission and the environment keep changing for each environment.
  ### Situation
   - The fuel-consuming area (fixed 40x40) remains and generate it randomly.
   - No diagonal movement, change parameter and object travel within one grid size.
   - Generate obstacles randomly with reasonable density.
   - Starting and Ending point are generated randomly (>= 40-unit in between)
   - Fuel-consuming area won't cover the obstacles and no obstacles should be generate at/near start and end point.

  ### Coding
  #### Firstly, remain only the fuel-consuming area and generate it randomly with a fixed area
  ![](https://i.postimg.cc/NjnBgS4Y/temp-Image8k-KWg-R.avif)

  #### Secondly, change robot radius so that the object could travel within one grid size
  ![](https://i.postimg.cc/BvhZ1t4W/temp-Image-Fmn0x-M.avif)

  #### Thirdly, create obstacles
  Use a loop to create totally 1200 obstacles that are not near the start and end points
  ![](https://i.postimg.cc/Z5RM5q7v/temp-Image-Wo-Rys-H.avif)

  #### Next, create destination and starting points randomly with at least a 40-unit distance in-between
  Use another loop to generate start and end points. But if the distance between them are not meet the requirement, delete them
  and create a new one
  
  ![](https://i.postimg.cc/L81jDKh0/temp-Image8uv96t.avif)

  #### To make sure plotting of the fuel-consuming area are not cover the obstacles, modify the code like this.
  First generate cost intensive area, then plot the start and end position
  ![](https://i.postimg.cc/QdQHVXFs/temp-Imagesf-FIUu.avif)

  ### Conclusion
  The final path is shown below, and we can also get total trip time in the terminal
  ![](https://i.postimg.cc/qRNxnhfW/temp-Image-Ijs-Bdt.avif)
  ![](https://i.postimg.cc/jjXFvJF5/temp-Imageg-ISu-Ke.avif)

## Task A3

## Reflections

  ### Lee Ching (24028115D)

  After completing this group project for the 1001 course, I learned a lot of things. First, I gained experience in teamwork and communication. I dedicated to communicating with classmates working on different parts of the project, discussing the content and design of our Github repository and powerpoint presentation. Some groupmates don't know what things they need to do, and I made an effort to explain what needed to be done. This allowed me to meet several new classmates. Secondly, I learned how to use Github. At first, I found that Github is quite eomplicated and didn't know how to use it. However, after becoming familiar with it, I discover that Github is a very convenient platform for group reports. I was responsible for designing the outline of our group's Github, allowing groupmates to directly add their content. At the same time, I also learned how to use Python. Although I had previously studied programming in other languages, getting the hang of a new language in a short time was still quite challenging. However, with the help of AL, I managed to learn quite a bit of Python syntax, which enabled me to complete the roadmap for Task 1. Overall, this group project was a great learning opportunity for me and provided me with a clear understanding of working on group projects.
  
  ### Song Yujie (24103111D)
  
  ### Kao Ching Yiu (24083458D)
  
  ### Ng Chi Hin (24083458D)

  ### Yang Yuqi (24106431D)

I have learned a lot in this group project. Firstly, this project has improved my programming ability. The project is a completely new subject for me, and I have never encountered it before. After careful reading, I found that this project is actually very interesting. For example, in task2, we need to design a time reduction area by ourselves. Since I have learned a little programming knowledge, this project has also been a good exercise for me to apply what I have learned to real research projects. Although there were many difficulties in the process, such as working hard to write the code but finding errors in running, after continuous modification, with the help of teachers and AI, the code of the task1-5 was successfully written, promoting the progress of our project. Besides, because it was a group project, I also got chance to know students from different places and had exchanges with them. I would like to thank the teachers of AAE1001 for giving us this opportunity and all the members of our group for their efforts in this group project.

  ### Lam Ho Lam (24078041D)

  ### Qaiser Katongole Mbidde (24111001D)

  ### Hui Long Wai (24084234D)

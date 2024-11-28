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

# Division of work:
1. Task 1: Lee Ching(24028115D) Yang Yuqi(24106431D) Hui Long Wai(24084234D)
2. Task 2: Yang Yuqi(24106431D) Kao Ching Yiu(24075232d) Song Yujie(24103111d)
3. Task 3: Lee Ching(24028115D) Song Yujie(24103111d) Lau Ho Lam(24078041d) Hui Long Wai(24084234D)
4. Task A1: Yang Yuqi(24106431D) Kao Ching YIu(24075232d)
5. Task A2: Yang Yuqi(24106431D)
6. Task A3: Qaiser Mbidde Katongole(24111001D)
7. Presentation slide: All of us


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

<img src="https://i.postimg.cc/Hx1CWHPS/obstacle1.png" alt="Obstacle" width="500"/>


By editing the python programme, we can find the shortest way:

<img src="https://i.postimg.cc/kXpzXq2x/image.png" alt="Obstacle" width="500"/>


To find the minimum cost, we have to use to following formula:

<img src="https://i.postimg.cc/0QnHgsgK/image.png" alt="Obstacle" width="500"/>

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

<img src="https://i.postimg.cc/T2ZYdypk/IMG-2060.jpg" alt="Obstacle" width="500"/>

  
### Coding

Click to enter the code interface

https://github.com/duqiu699/1001-group4/blob/main/Task%201

#### Firstly, set initial condition(start and goal position; border; cost intensive area)

<img src="https://i.postimg.cc/8CFqxCGz/temp-Image6-CO4-El.avif" alt="Obstacle" width="500"/>

<img src="https://i.postimg.cc/Zq11mhYF/temp-Imagee-GJYSE.avif" alt="Obstacle" width="500"/>

<img src="https://i.postimg.cc/G2G6hSH0/temp-Imageg-Rb-TK0.avif" alt="Obstacle" width="500"/>

#### Secondly, calculate trip cost
##### ---Input all data of three scenarios and use dictionary to encapsulate data of three types of aircrafts.

<img src="https://i.postimg.cc/25wz86JF/temp-Image-NT4-Ib-E.avif" alt="Obstacle" width="500"/>

##### ---Calculate the total cost if the flights number is eligible.

<img src="https://i.postimg.cc/yNYNRc0r/temp-Image-Gl-Rf66.avif" alt="Obstacle" width="500"/>

### Result

https://github.com/user-attachments/assets/d8126ef0-1882-4153-b054-a040701272db

https://github.com/user-attachments/assets/c24caba6-9e87-43fe-ac11-70b394057fbc

https://github.com/user-attachments/assets/fb234249-172f-4827-be9c-880d9200b41e


### Conclusion:

 * For scenario 1,the aircraft with the lowest operation cost is <ins>A330-900neo</ins>, it can conduct the amount of flight is <ins>$109128</ins>.
 * For scenario 2,the aircraft with the lowest operation cost is <ins>A350-900</ins>, it can conduct the amount of flight is <ins>$57568</ins>.
 * For scenario 3,the aircraft with the lowest operation cost is <ins>A321neo</ins>, it can conduct the amount of flight is <ins>$107117</ins>.



## Task 2

  In the following task, we are going to design a new cost area that can reduce the cost of the route.

  ### Jetstream
   A jet stream is a fast-flowing, narrow air current found in the atmosphere of some planets, including Earth. On Earth, jet streams are located near the altitude of the tropopause and are westerly winds (flowing west to east). Their paths typically have a meandering shape and can be thousands of kilometers long, a few hundred kilometers wide, and a few kilometers deep.

   <img src="https://i.postimg.cc/FRGmT8DD/image.png" alt="Obstacle" width="500"/>
  https://svs.gsfc.nasa.gov/3864

  ### Background

  By using the same obstacle set and scenario 1 in task 1, we are going to find the best place to set our minus-cost-area(jetstream) for this test, while the cost in jetstream area can be reduced by 5%. The area of jetstream will span across the map laterally and span 5-unit length vertically.
  

  By editing programme, we can find the best place of Jetstream:

    <img src="https://i.postimg.cc/G2MwFYmf/image.png" alt="Obstacle" width="500"/>

  ### Coding
  
  Click to enter the code interface
  
  https://github.com/duqiu699/1001-group4/blob/main/Task%202
  
  #### Firstly，add a third code to modify the cost

  <img src="https://i.postimg.cc/GpQ7XQYT/temp-Image1-TTOAy.avif" alt="Obstacle" width="500"/>
  
  #### Secondly, add less cost in jet stream by mimicing the code of cost intensive area

  <img src="https://i.postimg.cc/PNsQXpYk/temp-Imagevmv-Ysq.avif" alt="Obstacle" width="500"/>
  
  #### Thirdly, set cost reduced area 3.
  We can change the number in the second line of code to change the position of jet stream.

  <img src="https://i.postimg.cc/jSCPp4GJ/temp-Image-Yr-BWxe.avif" alt="Obstacle" width="500"/>
  
  #### Lastly, plot the cost reduced area 3

  <img src="https://i.postimg.cc/k4w5MkSM/temp-Imagenf-Sy-XK.avif" alt="Obstacle" width="500"/>

  ### Result
  
https://github.com/user-attachments/assets/41c0d3a9-e654-41fb-a401-756f698a7802


  
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

  ### Our steps in calculation
1. Find out the total flight time for the flight path, which is about 105.0538 minutes according to the result of Task 1.
2. By obtaining that result, Taiwan Taoyuan International Airport (TPE) is chosen as our destination, departing from Hong Kong Innternational Airport (HKG).
3. According to the IATA Fuel Price Analysis as followed, the jet fuel price for flights that departure from Asian areas is about US$105.68/barrel. After calculation, the fuel cost is found to be US$0.78/kg.
  <img src="https://i.postimg.cc/PrtQXHC7/3.png" alt="Obstacle" width="800"/>
  
4. Find out the time cost US$/min for each 50 passengers (e.g. US$12 for the aircraft that carries 100 passengers, US$14 for the aircraft that carries 150 passengers etc.).

The results of the above steps are shown in the below table:

  <img src="https://i.postimg.cc/pr9x84rM/1.png" alt="Obstacle" width="800"/>
  
5. Find out the number of flights needed to carry 3000 passengers in a week for each type of aircraft. As the maximum flights set for a week is 12, aircraft that carries 100, 150 and 200 passengers should be eliminated (required 30, 20, 15 flights respectively for a week.)

6. Find out the time cost, fuel cost and the total cost by serious calculation.

  ### Results
  After comparison of the total cost for each type of aircraft (shown below), aircraft that carries 450 passengers should be chosen. 
  
  <img src="https://i.postimg.cc/Jns4cGYF/2.png" alt="Obstacle" width="800"/>
  The new type aircraft designed will be named after A350 Pro Max, which has 4 engines itself, and can carry 450 passengers. The design of the aircraft, which is generated by ChatGPT, is shown below.
  
  
  <img src="https://i.postimg.cc/SxR5KCnH/4.png" alt="Obstacle" width="800"/>


## Task A1
  In the following task, the aircraft will be a supply craft that must reach 2 drop-off points to drop supplies before heading to base.
  ### Situation
  - One checkpoint should be added in cost intensive area
  - All checkpoint need to be reached before arriving at the destination.

  ### Coding
Click to enter the code interface

https://github.com/duqiu699/1001-group4/blob/main/Task%20A1
  
  #### Firstly, add one checkpoint for each cost intensive area
  <ins>cp1x</ins> and <ins>cp1y</ins> are for checkpoint1, <ins>cp2x</ins> and <ins>cp2y</ins> are for checkpoint2
  we can also adjust the checkpoint by change the number
  
   <img src="https://i.postimg.cc/rpq32J6c/temp-Imagew-Hs-J3-C.avif" alt="Obstacle" width="500"/>


  #### Secondly, reach all checkpoints before arriving at the destination
  Because of the aircraft need to each all checkpoints before arriving at the destination, we can divide the path into three parts, calculate the time spent on each part and add it together to get the total time.
  
   <img src="https://i.postimg.cc/ZY6Qn2TZ/temp-Image-Fx-Arqa.avif" alt="Obstacle" width="500"/>

   ### Result
   
https://github.com/user-attachments/assets/a1930a31-6112-446d-ac06-e6f2d32dcdca

  ### Conclusion
  The finally path and output are in the following pictures.
  the checkpoints shows before the path display
  
   <img src="https://i.postimg.cc/4NBBhTjC/temp-Image-Dr-Jw-Om.avif" alt="Obstacle" width="500"/>

   <img src="https://i.postimg.cc/vHB5kx2j/temp-Image-Jk6b-M4.avif" alt="Obstacle" width="500"/>
   
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
Click to enter the code interface

https://github.com/duqiu699/1001-group4/blob/main/Task%20A2
  #### Firstly, remain only the fuel-consuming area and generate it randomly with a fixed area

   <img src="https://i.postimg.cc/NjnBgS4Y/temp-Image8k-KWg-R.avif" alt="Obstacle" width="500"/>

  #### Secondly, change robot radius so that the object could travel within one grid size

   <img src="https://i.postimg.cc/BvhZ1t4W/temp-Image-Fmn0x-M.avif" alt="Obstacle" width="500"/>

  #### Thirdly, create obstacles
  Use a loop to create totally 1200 obstacles that are not near the start and end points

   <img src="https://i.postimg.cc/Z5RM5q7v/temp-Image-Wo-Rys-H.avif" alt="Obstacle" width="500"/>

  #### Next, create destination and starting points randomly with at least a 40-unit distance in-between
  Use another loop to generate start and end points. But if the distance between them are not meet the requirement, delete them
  and create a new one
  
   <img src="https://i.postimg.cc/L81jDKh0/temp-Image8uv96t.avif" alt="Obstacle" width="500"/>

  #### To make sure plotting of the fuel-consuming area are not cover the obstacles, modify the code like this.
  First generate cost intensive area, then plot the start and end position
  
   <img src="https://i.postimg.cc/QdQHVXFs/temp-Imagesf-FIUu.avif" alt="Obstacle" width="500"/>

   ### Result

https://github.com/user-attachments/assets/228cbeb6-7baf-4892-82f3-329af438d6dc

  ### Conclusion
  Here are two examples. The final path is shown below, and we can also get total trip time in the terminal

   <img src="https://i.postimg.cc/qRNxnhfW/temp-Image-Ijs-Bdt.avif" alt="Obstacle" width="500"/>

   <img src="https://i.postimg.cc/jjXFvJF5/temp-Imageg-ISu-Ke.avif" alt="Obstacle" width="500"/>

   <img src="https://i.postimg.cc/prH35VQC/temp-Imagej-TUY0-P.avif" alt="Obstacle" width="500"/>

   <img src="https://i.postimg.cc/mr1nd18V/temp-Imagek-Np-M8-Q.avif" alt="Obstacle" width="500"/>


## Task A3

## Reflections

  ### Lee Ching (24028115D)

  After completing this group project for the 1001 course, I learned a lot of things. First, I gained experience in teamwork and communication. I dedicated to communicating with classmates working on different parts of the project, discussing the content and design of our Github repository and powerpoint presentation. Some groupmates don't know what things they need to do, and I made an effort to explain what needed to be done. This allowed me to meet several new classmates. Secondly, I learned how to use Github. At first, I found that Github is quite eomplicated and didn't know how to use it. However, after becoming familiar with it, I discover that Github is a very convenient platform for group reports. I was responsible for designing the outline of our group's Github, allowing groupmates to directly add their content. At the same time, I also learned how to use Python. Although I had previously studied programming in other languages, getting the hang of a new language in a short time was still quite challenging. However, with the help of AL, I managed to learn quite a bit of Python syntax, which enabled me to complete the roadmap for Task 1. Overall, this group project was a great learning opportunity for me and provided me with a clear understanding of working on group projects.
  
  ### Song Yujie (24103111D)
  At first, I didn't know anything about programming, but after a period of study, I gradually mastered the basic syntax of Python and some common libraries, trying to solve the problems assigned to the task1 and task2. Every successful practice gives me great information and a sense of accomplishment. But after all, I'm just a beginner, and in the end, I chose the most concise and comprehensive program in the group. But that has opened the door for me to python, and I'm not going to stop there. Also, in the process of completing the group tasks, we enlisted AI help. The AI interprets programs we don't understand and provides divergent ideas, which not only enhances our programming skills, but also broadens my horizons。 I am grateful for every team mumbers's effort. without everyone's concerted efforts, this task cannot be completed.
  ### Kao Ching Yiu (24075232D)
  During this period of this group project, I gain many experience and learn a lot. To start with, I learnt how to communicate and collaborate with my teammates. For example, I was mainly assisting my groupmate in task 2 and task A1, in task A1, the coding is base on the code in task 2 and enhance a bit of it. My teammate is good at coding part therefore I assist them with the data input and the silde making process. We distributed all the work base on our ability, because of that we can finish our part effectively and have more times to deal with the difficult part all of us faced. All of these is the benefits of teamworking. Apart from that, I also learnt how to coding and use Python for program. I was a beginner in github and coding so I ask AI and my groupmate to help and I finally understand the basic knowledge of coding and programming. I found that coding actually save us a lot of time and efford in the calculating and finding relation process. I am willing to learn more about these useful tools, which is coding and AI.
  
  ### Ng Chi Hin (24083458D)

  ### Yang Yuqi (24106431D)

I have learned a lot in this group project. Firstly, this project has improved my programming ability. The project is a completely new subject for me, and I have never encountered it before. After careful reading, I found that this project is actually very interesting. For example, in task2, we need to design a time reduction area by ourselves. Since I have learned a little programming knowledge, this project has also been a good exercise for me to apply what I have learned to real research projects. Although there were many difficulties in the process, such as working hard to write the code but finding errors in running, after continuous modification, with the help of teachers and AI, the code of the task1-5 was successfully written, promoting the progress of our project. Secondly, I have learned how to use github and write github page. This experience makes me get familiar with github, and I think if I have opportunity in the future, I will also open my own github to record my life or research. At the same time, github has a lot of code uploaded by others for us to use, which will also become my learning database. Lastly, because it was a group project, I also got chance to know students from different places and had exchanges with them. I would like to thank the teachers of AAE1001 for giving us this opportunity and all the members of our group for their efforts in this group project.

  ### Lam Ho Lam (24078041D)
The group project for AAE1001 is an enriching and enlightening experience. The project was supposed to involve inputting the data, carrying out some cost calculations, and developing an optimal aircraft for a given scenario. This helped me truly internalize aviation concepts, decision-making, and how engineering principles are applied in reality. It was complicated at the beginning because we needed to balance so many factors: cost, carrying, and fuel usage, but it has been easy because, in teamwork, we went step by step; we divided and took our responsibilities to allow progress to be ensured. For me, I was doing the data input and cost analysis, which gave me a great insight into the fields of accuracy and attention to detail. A small mistake in the input would have given entirely different results to show why precision is key in any engineering task. One of the major aspects of the project was selecting the optimal airplane. This required meaningful discussion and collaboration since we suggested various ones and justified our selection with some specifications. The experience enriched my problem-solving skills and my capability for evidence-based decisions. In the process, the project helped me get more technical knowledge, and it also improved my communication and teamwork skills. The project was a great learning experience that showed me the importance of teamwork and careful analysis necessary to solve real engineering problems.

  ### Qaiser Katongole Mbidde (24111001D)

  ### Hui Long Wai (24084234D)

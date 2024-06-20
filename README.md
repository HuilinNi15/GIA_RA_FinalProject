# GIA_RA_FinalProject

<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> Table of Contents </h2>

<details open="open">
  <summary> Table of Contents </summary>
  <ol>
    <li><a href="#about-the-project"> About the project </a></li>
    <li><a href="#prerequisites"> Prerequisites </a></li>
    <li><a href="#part-1"> Part 1: Path Planning and Manipulation with an UR3a </a></li>
    <li><a href="#part-2"> Part 2: Mobile Robotics with a Waffle_Pi </a></li>
     <li><a href="#contributors"> Contributors </a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> 📝 About The Project</h2>

<p align="justify"> 
   This project consists in 2 parts: 
   - **Part 1**: Path Planning and Manipulation with an UR3a
   - **Part 2**: Mobile Robotics with a Waffle_Pi
</p>


<!-- Prerequisites -->
<h2 id="prerequisites"> 🛠️ Prerequisites </h2>

<h3> Part 1: Path Planning and Manipulation with an UR3a </h3>

To install The Kautham Project:
```
$ sudo add-apt-repository ppa:deb-rob/focal-robotics
$ sudo apt-get update
$ sudo apt-get install kautham kautham-tools kautham-ros-osrf kautham-demos-osrf python3-kautham-ros
$ sudo apt-get upgrade
```

<h4> To install the task_and_motion_planning github and its dependencies: </h4>

1. Install the required dependencies for the FF server:
   ```
   $ sudo apt install flex bison libpugixml-dev
   ``` 
2. Install Python3, required by the ktmpb package:
   ```
   $ sudo apt-get install python3-pip python3-yaml
   $ sudo pip3 install rospkg catkin_pkg
   $ sudo pip3 install transformations
   $ sudo pip3 install pytransform3d
   ```
3. Clone the task and movement planning meta-repository:
   ```
   $ mkdir git-projects
   $ cd git-projects
   $ git clone --single-branch --branch=planningcourse https://gitioc.upc.edu/rostutorials/task_and_motion_planning.git
   $ cd task_and_motion_planning
   $ git submodule init
   $ git submodule update
   $ cd
   ```
4. Create a catkin workspace for the exercises in this tutorial and create a symbolic link to the packages we will use:
   ```
   $ mkdir -p catkin_wsTAMP/src
   $ cd catkin_wsTAMP/src
   $ ln -s ~/git-projects/task_and_motion_planning
   $ cd..
5. Next, build the packages:
   ```
   $ catkin build
   $ source devel/setup.bash
   ```
   
<h3> Part 2: Mobile Robotics with a Waffle_Pi </h3>

Install ROS Noetic
~~~
$ sudo apt update
$ sudo apt upgrade
$ wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_noetic.sh
$ chmod 755 ./install_ros_noetic.sh
$ bash ./install_ros_noetic.sh
~~~ 

Install Dependent ROS Packages
```
$ sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
ros-noetic-rosserial-python ros-noetic-rosserial-client \
ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```

Install TurtleBot3 Packages
```
$ sudo apt install ros-noetic-dynamixel-sdk
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3
```

Install Simulation Package
```
$ cd ~/catkin_ws/src/
$ git clone -b kinetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ source /opt/ros/noetic/setup.bash
$ cd ~/catkin_ws && catkin_make
$ cd ~/catkin_ws/src/
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
$ cd ~/catkin_ws && catkin_make
$ cd ~/catkin_ws/src/
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make
```

<!-- Part 1: Path Planning and Manipulation with an UR3a-->
<h2 id="part-1"> 🦾 Part 1: Path Planning and Manipulation with an UR3a </h2>

This part of the project focuses on programming a robot manipulator to execute certain tasks. We have modeled a chess-like scenario where the robot respects the turn-taking of the pieces (white-black) and moves the chess pieces according to their legal moves. Specifically, we have modeled the pawn, knight, and king. The steps involved are:

1. **Task Design**: Design a couple of tasks that a robot manipulator (specifically the UR3e in our case) can execute. The tasks involve moving chess pieces according to the rules of chess.
2. **PDDL Files Creation**: Create the domain and problem files (PDDL) associated with these tasks. We have created three problem files, each with a different scenario where the robot has to move the pieces from their original positions to their goal positions while respecting the turns of the pieces.
3. **Planning Problem Solving**: Solve the task and motion planning problems associated with each problem file. The motion planning part needs to be addressed using different planners.
4. **Simulation Comparison**: Compare the obtained solutions in simulation using The Kautham Project.
5. **Benchmarking Study**: Conduct a benchmarking study with the planners used to evaluate their performance. We have used the [**Planner Arena**](https://plannerarena.org/) website to visualize the boxplots with the times of each planner. 

In our specific implementation, we have modeled only basic movements. One team cannot "capture" the pieces of the other team, nor perform any special moves; only simple, legal moves are considered.

<!-- Part 2: Mobile Robotics with a Waffle_Pi -->
<h2 id="part-2"> 🤖 Part 2: Mobile Robotics with a Waffle_Pi </h2>

This part of the project focuses on a navigation task for the robot. Examples of such tasks include:

- Exploration of unknown areas
- Following people with a camera
- Searching for objects
- etc.

In our case, our Waffle Pi robot recognizes three different colors (yellow, green and red). The process involves:

1. **Color Recognition**: The robot identifies colors using our custom color_viewer node, which detects the colors yellow and red.
2. **Color Publishing**: The detected color is published, and the the color_mover node is subscribed to get this color.
3. **Action Based on Color**: The color_mover node associates the given color with a specific action:
   - If the color is **yellow**, the robot raises its arm (the driver).
   - If the color is **green**, the robot spins with a certain angular velocity during a certain time. 
   - If the color is **red**, the robot stops for 10 seconds.
4. **Obstacle Avoidance**: The robot moves straight continuously until it needs to avoid an obstacle, using the move_base topic for navigation adjustments.

To execute our code, you need to execute the following commands: 

If you want to execute it in simulation: 
```
T1: $ roscore
T2: $ roslaunch turtlebot3_gazebo turtlebot3_world.launch 
T3: $ roslaunch turtlebot3_slam turtlebot3_slam.launch
T4: $ roslaunch turtlebot3_navigation move_base.launch
T5: $ rosrun color_viewer color_viewer.py
T6: $ rosrun color_mover color_mover.py
```

If you want to execute the code with a Waffle Pi robot: 
```
T1: roscore
T2: ssh ubuntu@<waffle_pi_IP>
    roslaunch turtlebot3_bringup turtlebot3_robot.launch
T3: ssh ubuntu@<waffle_pi_IP>
    roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch
T4: $ roslaunch turtlebot3_slam turtlebot3_slam.launch
T5: $ roslaunch turtlebot3_navigation move_base.launch
T6: $ rosrun color_viewer color_viewer.py
T7: $ rosrun color_mover color_mover.py
```
Make sure that the PC is connected correctly to the robot's IP and that both of them are connected to the same network.

<!-- Contributors -->
<h2 id="contributors"> 👥 Contributors</h2>

* [**Huilin Ni**](https://github.com/HuilinNi15)
* [**Sergi Guimerà Roig**](https://github.com/S3RXxX)
* [**Núria Bosch Martínez**](https://github.com/nuriaboma)
* [**Amadeo Huerta Moncho**](https://github.com/amadeohm)
* [**Sandra Jiménez Vargas**](https://github.com/SandraJimenez231203)

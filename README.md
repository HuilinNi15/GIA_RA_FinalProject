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
  With this project we aim to ... 

   This project consists in 2 parts: 
   - Part 1: Path Planning and Manipulation with an UR3a
   - Part 2: Mobile Robotics with a Waffle_Pi
</p>


<!-- Prerequisites -->
<h2 id="prerequisites"> 🛠️ Prerequisites </h2>

<h3> Part 1: Path Planning and Manipulation with an UR3a </h3>

<h4> To install The Kautham Project: </h4>
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

<h4> Install ROS Noetic </h4>
```
$ sudo apt update
$ sudo apt upgrade
$ wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_noetic.sh
$ chmod 755 ./install_ros_noetic.sh
$ bash ./install_ros_noetic.sh
```

<h4> Install Dependent ROS Packages </h4>
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

<h4> Install TurtleBot3 Packages </h4>
```
$ sudo apt install ros-noetic-dynamixel-sdk
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3
```

<h4> Install Simulation Package </h4>
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


<!-- Part 2: Mobile Robotics with a Waffle_Pi -->
<h2 id="part-2"> 🤖 Part 2: Mobile Robotics with a Waffle_Pi </h2>


<!-- Contributors -->
<h2 id="contributors"> 👥 Contributors</h2>

* [**Huilin Ni**](https://github.com/HuilinNi15)
* [**Sergi Guimerà Roig**](https://github.com/S3RXxX)
* [**Núria Bosch Martínez**](https://github.com/nuriaboma)
* [**Amadeo Huerta Moncho**](https://github.com/amadeohm)
* [**Sandra Jiménez Vargas**](https://github.com/SandraJimenez231203)


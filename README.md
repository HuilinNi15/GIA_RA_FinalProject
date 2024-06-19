# GIA_RA_FinalProject
## P1-Manipulacion
### Packages needed
---
To install The Kautham Project:
```
$ sudo add-apt-repository ppa:deb-rob/focal-robotics
$ sudo apt-get update
$ sudo apt-get install kautham kautham-tools kautham-ros-osrf kautham-demos-osrf python3-kautham-ros
$ sudo apt-get upgrade
```

To install the task_and_motion_planning github and its dependencies: 

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
   
## P2-RoboticaMovil
---

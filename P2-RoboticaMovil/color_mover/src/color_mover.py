#!/usr/bin/env python3
import rospy
import roslib
import numpy as np
from std_msgs.msg import Int8
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback
import actionlib
from geometry_msgs.msg import Twist
# from sensor_msgs.msg import LaserScan  # podem afegir el Laser per decidir millor com actuar
from std_srvs.srv import Empty
from trajectory_msgs.msg import JointTrajectory  # pel braç
from trajectory_msgs.msg import JointTrajectoryPoint

class color_mover:
    def __init__(self) -> None:
        rospy.loginfo("Started color mover node")
        self.l = 0.3
        self.map_colors = {0: None, 1: "red", 2: "green", 3: "blue", 4: "yellow"}
        
        self.sub = rospy.Subscriber('integer_topic', Int8, callback=self.color_callback, queue_size=1)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # self.armpub = rospy.Publisher('/joint_trajectory_point', JointTrajectory, queue_size=10)
        # self.trajectory_msg = JointTrajectory()
        # self.trajectory_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']
        # self.point = JointTrajectoryPoint()
        # point.time_from_start = rospy.Duration(1.0)

        self.move_base_client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
        self.move_base_client.wait_for_server() 
        rospy.loginfo("move_base loaded")

        self.goal = MoveBaseGoal()
        self.goal.target_pose.pose.orientation.w = 1
        
        rospy.loginfo("Clearing space")
        self.clear_unknown_space()
        rospy.loginfo("Space cleared")
        
    def move_arm(self, coords):
        "donada la posició del braç, moure'l allà"
        # self.point.positions = coords
        # self.trajectory_msg.points.append(point)
        # self.pub.publish(self.trajectory_msg)
        pass

    def stop_robot(self, duration=3):
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = 0
        self.cmd_vel_pub.publish(twist)
        rospy.sleep(duration)
    
    def clear_unknown_space(self):
        rospy.wait_for_service('clear_unknown_space')
        try:
            clear_service = rospy.ServiceProxy('clear_unknown_space', Empty)
            clear_service()
            rospy.loginfo("Unknown space cleared successfully.")
        except rospy.ServiceException as e:
            rospy.logerr(f"Service call failed: {e}")

    def move_to_goal(self, x, y, wait=False):
        """
        Passades unes coordenades x, y respecte la base del robot les passa 
        a move_base per planificar el moviment
        """ 
        rospy.loginfo(f"goal {self.goal}")
        self.goal.target_pose.header.frame_id = "base_link"
        
        self.goal.target_pose.pose.position.x = x
        self.goal.target_pose.pose.position.y = y
    
            
        self.move_base_client.send_goal(self.goal)
        if wait: # esperar o no,  aquesta es la questio
            self.move_base_client.wait_for_result()
    
    def color_callback(self, messages):
        color_int = messages.data
        self.color = self.map_colors[color_int]
        rospy.loginfo(f"Received color {self.color}")
        rospy.loginfo(f"l value: {self.l}")

        if self.color is None:
            self.move_to_goal(self.l, 0, wait=False)  

        elif self.color == "red":
            self.stop_robot(3)
            self.move_to_goal(self.l, 0, wait=True)
        elif self.color == "green":
            self.move_to_goal(0, self.l, wait=True)
        elif self.color == "blue":
            self.move_to_goal(0, -self.l, wait=True)
        elif self.color == "yellow":
            # self.move_arm([])
            # self.move_to_goal(self.l, self.l, wait=True)
            # self.move_arm([])

            rospy.loginfo("NOT IMPLEMENTED YET")  # Placeholder for arm movement
        else:
            rospy.logerr(f"Unsupported color action for {self.color}")

if __name__== "__main__":
    rospy.init_node("color_mover_node")
    cm = color_mover()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("ROS Interrupt Exception")
        
        
        
        

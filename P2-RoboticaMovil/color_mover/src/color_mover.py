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

class color_mover:
    def __init__(self) -> None:
        rospy.loginfo("Started color mover node")
        self.map_colors = {0: None, 1: "red", 2: "green", 3: "blue", 4: "yellow"}
        
        self.sub = rospy.Subscriber('integer_topic', Int8, callback=self.color_callback)
        self.move_base_client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
        self.move_base_client.wait_for_server() 
        rospy.loginfo("move_base loaded")

        self.goal = MoveBaseGoal()
        self.goal.target_pose.pose.orientation.w = 1
        self.l = 0.3
        self.color_detected = False  # Make sure this is defined before any callback can occur
        self.color = None  # Initialize self.color as well

        rospy.loginfo("Clearing space")
        self.clear_unknown_space()
        rospy.loginfo("Space cleared")
        
    def move_arm(self):
        "donada la posició del braç, moure'l allà"
        pass
    
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
        if self.color_detected:
            self.goal.target_pose.pose.position.x = x
            self.goal.target_pose.pose.position.y = y
        else:
            self.goal.target_pose.pose.position.x = self.l
            self.goal.target_pose.pose.position.y = 0
            
        self.move_base_client.send_goal(self.goal)
        if wait: # esperar o no,  aquesta es la questio
            self.move_base_client.wait_for_result()
    
    def color_callback(self, messages):
        color_int = messages.data
        self.color = self.map_colors[color_int]
        rospy.loginfo(f"Received color {self.color}")
        rospy.loginfo(f"l value: {self.l}")

        if self.color is None:
            # If no color is detected, move forward
            self.move_to_goal(0, self.l, wait=False)
            self.color_detected = False
        else:
            # Color is detected, process according to color
            self.color_detected = True
            if self.color == "red":
                rospy.sleep(3)
                self.move_to_goal(0, self.l, wait=True)
            elif self.color == "green":
                self.move_to_goal(self.l, 0, wait=True)
            elif self.color == "blue":
                self.move_to_goal(-self.l, 0, wait=True)
            elif self.color == "yellow":
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
        
        
        
        

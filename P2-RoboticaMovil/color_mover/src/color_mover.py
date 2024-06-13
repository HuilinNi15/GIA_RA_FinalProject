#!/usr/bin/env python3
import rospy
import roslib
import numpy as np
from std_msgs.msg import Int8
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback
import actionlib
from geometry_msgs.msg import Twist
# from sensor_msgs.msg import LaserScan  # podem afegir el Laser per decidir millor com actuar

class color_mover:
    def __init__(self) -> None:
        rospy.loginfo("Started color mover node")
        self.map_colors = {0: None, 1: "red", 2: "green", 3: "blue"} ## es pot canviar per una llista
        
        self.sub = rospy.Subscriber('integer_topic', Int8,callback=self.color_callback)
        
        self.move_base_client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
        self.move_base_client.wait_for_server()

        rospy.loginfo("move_base loaded")

        self.goal = MoveBaseGoal()
        self.goal.target_pose.pose.orientation.w = 1

    def move_to_goal(self, x, y):
        """
        Passades unes coordenades x, y respecte la base del robot les passa 
        a move_base per planificar el moviment
        """ 
        self.goal.target_pose.header.frame_id = "base_link"
        self.goal.target_pose.pose.position.x = x
        self.goal.target_pose.pose.position.y = y
        self.move_base_client.send_goal(self.goal)
        rospy.loginfo(f"goal sent, waiting for result {self.c}")
        self.move_base_client.wait_for_result()
    
    def color_callback(self, messages):
        color_int = messages.data
        self.color = self.map_colors[color_int]
        rospy.loginfo(f"Recieved color {self.color}")
        
        ### fer if

        if not self.color:
            self.move_to_goal(0, 1)
        elif self.color == "red":
            pass
            # self.move_to_goal()
        elif self.color == "green":
            self.move_to_goal(0, 1)
        elif self.color == "blue":
            pass
        else:
            pass  # raise not implemented error


if __name__== "__main__":
    np.random.seed(373)
    rospy.init_node("color_mover_node")
    color_mover()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("ROS Interrupt Exception")
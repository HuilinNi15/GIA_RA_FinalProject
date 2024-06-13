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
        self.map_colors = {0: None, 1: "red", 2: "green", 3: "blue", 4: "yellow"} ## es pot canviar per una llista
        
        self.sub = rospy.Subscriber('integer_topic', Int8,callback=self.color_callback)
        
        self.move_base_client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
        
        self.move_base_client.wait_for_server() 

        rospy.loginfo("move_base loaded")

        self.goal = MoveBaseGoal()
        self.goal.target_pose.pose.orientation.w = 1
        self.l = 0.3
    
    def move_arm(self):
        "donada la posició del braç, moure'l allà"
        pass

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
        rospy.loginfo(f"Recieved color {self.color}")
        
        if not self.color:
            # si no hi ha res tirar endavant
            self.move_to_goal(0, self.l, wait=False)
        elif self.color == "red": ## parar 3 segons
            rospy.sleep(3)
            self.move_to_goal(0, self.l, wait=False)
        elif self.color == "green":  ## girar esquerra (n dist a esq)
            self.move_to_goal(self.l, 0, wait=False)
        elif self.color == "blue":  ## girar dreta (n dist a dreta)
            self.move_to_goal(-self.l, 0, wait=False)
        elif self.color == "yellow":
            """self.move_arm()
            self.move_to_goal(0, self.l, wait=True)
            self.move_arm"""
            rospy.loginfo("NOT IMPLEMENTED YET") # aixecar el braç
        else:
            raise ValueError('NOT IMPLEMENTED')


if __name__== "__main__":
    np.random.seed(373)
    rospy.init_node("color_mover_node")
    color_mover()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("ROS Interrupt Exception")
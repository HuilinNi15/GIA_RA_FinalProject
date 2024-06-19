#!/usr/bin/env python3
import rospy
import roslib
import numpy as np
from std_msgs.msg import Int8, Float64MultiArray
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback
import actionlib
from geometry_msgs.msg import Twist
# from sensor_msgs.msg import LaserScan  # podem afegir el Laser per decidir millor com actuar
from std_srvs.srv import Empty


class color_mover:
    def __init__(self) -> None:
        rospy.loginfo("Started color mover node")
        self.l = 0.3
        self.map_colors = {0: None, 1: "red", 2: "green", 3: "yellow"}
        
        self.sub = rospy.Subscriber('integer_topic', Int8, callback=self.color_callback, queue_size=1)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.armpub = rospy.Publisher('/joint_trajectory_point', Float64MultiArray, queue_size=10)
        self.arm_msg = Float64MultiArray()
        
        self.arm_msg.data = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.armpub.publish(self.arm_msg)

        self.move_base_client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
        self.move_base_client.wait_for_server() 
        rospy.loginfo("move_base loaded")

        self.goal = MoveBaseGoal()
        self.goal.target_pose.pose.orientation.w = 1
        
        rospy.loginfo("Clearing space")
        self.clear_unknown_space()
        rospy.loginfo("Space cleared")
        
    def move_arm(self, start_coords, end_coords,  steps=123):
        "Mueve el brazo desde start_coords hasta end_coords en un tiempo determinado"
        increment = np.array([(end_coords[i]-start_coords[i])/steps for i in range(len(start_coords))])
        coords = np.array(start_coords)
        for _ in range(steps):
            coords = coords + increment
            self.arm_msg.data = coords
            self.armpub.publish(self.arm_msg)
            rospy.sleep(5/steps)

    
    def stop_robot(self, duration=3):
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = 0
        self.cmd_vel_pub.publish(twist)
        rospy.sleep(duration)
    def do_spin(self, t=1, w=2.5):
        twist = Twist()
        twist.linear.x = 0.001
        twist.angular.z = w
        self.cmd_vel_pub.publish(twist)
        rospy.sleep(t)
    
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

        if self.color is None:
            self.move_to_goal(self.l, 0, wait=False)  

        elif self.color == "red":
            self.stop_robot(10)
            self.move_to_goal(self.l/3, 0, wait=True)
        elif self.color == "green":
            self.do_spin(t=1)
            self.stop_robot(3)
            self.move_to_goal(self.l/3, 0, wait=True)
        elif self.color == "yellow":
            self.move_arm([0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.5, 0.3])
            self.move_to_goal(self.l, 0, wait=False)
            self.move_arm([0.0, 0.0, 0.0, -0.5, 0.3], [0.0, 0.0, 0.0, 0.0, 0.0])

        else:
            rospy.logerr(f"Unsupported color action for {self.color}")
            

if __name__== "__main__":
    rospy.init_node("color_mover_node")
    cm = color_mover()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("ROS Interrupt Exception")
        
        
        
        

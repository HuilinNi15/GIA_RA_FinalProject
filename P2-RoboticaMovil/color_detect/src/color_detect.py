#!/usr/bin/env python3
import rospy
import roslib
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

class ColorHandler:
    def __init__(self) -> None:
        rospy.loginfo("Started color handler node")

        self.colors = {"red":np.array([95, 55, 226]), "green":np.array([50, 181, 91]), "blue": np.array([250, 0, 0]), "yellow": np.array([36, 161, 183])} #bgr en cv2
        self.map_colors = {None: 0, "red": 1, "green": 2, "blue": 3, "yellow": 4, 0: None, 1: "red", 2: "green", 3: "blue", 4: "yellow"}
        self.color_threshold = 75
        self.pixel_count_threshold = 3000 # amb color vermell el threshold està be a 23000
        self.step = 1 
        self.bridge_object = CvBridge()

        self.color = None
        
        self.image_sub = rospy.Subscriber("/camera/image", Image, self.camera_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.goal = MoveBaseGoal()
        self.goal.target_pose.pose.orientation.w = 1
        
        self.move_base_client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
        self.move_base_client.wait_for_server() 
        rospy.loginfo("move_base loaded")
        
        rospy.loginfo("Clearing space")
        self.clear_unknown_space()
        rospy.loginfo("Space cleared")
   
    ###################################
    ### methods for BGR colors#########
    ###################################
    def color_distance(self, c1, c2):
        return np.sqrt(np.sum((c1 - c2) ** 2))
    
    def check_1_color(self, color_str, pixel):
        return self.color_threshold >= self.color_distance(self.colors[color_str], pixel)

    def check_colors(self):
        c = {color_str: 0 for color_str in self.colors}
        sampled_image = self.crop_image()
        for row in sampled_image:
            for pixel in row:
                for color_str in self.colors:
                    c[color_str] += self.check_1_color(color_str, pixel)*self.step
        m = max(c, key=c.get)
        self.color = m if c[m] > self.pixel_count_threshold else None

        rospy.loginfo("")
        rospy.loginfo(f"{c}")
        rospy.loginfo("")

    def crop_image(self):
        height, width, channels = self.image.shape
        descentre = height // 4
        rows_to_watch = height // 2
        cropped_image = self.image[(height)//2+descentre:(height), width//5:4*width//5]
        rospy.loginfo(f"{self.image.shape} --> {cropped_image.shape}")
        return cropped_image

    def camera_callback(self, messages):
        try:
            self.image = self.bridge_object.imgmsg_to_cv2(messages, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)
        
        self.check_colors()
        if self.color:
            rospy.loginfo(f"Found color {self.color}")
        else:
            rospy.loginfo("No signal color found")

        self.handle_color_action()

    def move_arm(self, coords):
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
        rospy.loginfo(f"goal {self.goal}")
        self.goal.target_pose.header.frame_id = "base_link"
        
        self.goal.target_pose.pose.position.x = x
        self.goal.target_pose.pose.position.y = y
    
        self.move_base_client.send_goal(self.goal)
        if wait:
            self.move_base_client.wait_for_result()
        self.stop_robot(1)
    
    def handle_color_action(self):
        rospy.loginfo(f"Handling action for color {self.color}")

        if self.color is None:
            self.move_to_goal(0.1, 0, wait=False)  
            
        elif self.color == "red":
            self.stop_robot(10)
            self.move_to_goal(0.1, 0, wait=True)
            
        elif self.color == "green":
            self.move_to_goal(0, 0.08, wait=True)
            
        elif self.color == "blue":
            self.move_to_goal(0, -0.1, wait=True)
            
        elif self.color == "yellow":
            rospy.loginfo("NOT IMPLEMENTED YET")
        
        else:
            rospy.logerr(f"Unsupported color action for {self.color}")

if __name__== "__main__":
    rospy.init_node("color_handler_node")
    ch = ColorHandler()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("ROS Interrupt Exception")


#!/usr/bin/env python3
import rospy
import roslib
import numpy as np
import cv2
import sys
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import Int8
# from geometry_msgs.msg import Twist
# from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback
# import actionlib


class color_viewer:
    def __init__(self) -> None:
        rospy.loginfo("Started color viewer node")

        self.colors = {"red":np.array([95, 55, 226]), "green":np.array([50, 181, 91]), "blue": np.array([250, 0, 0]), "yellow": np.array([36, 161, 183])} #bgr en cv2
        self.map_colors = {None: 0, "red": 1, "green": 2, "blue": 3, "yellow": 4}
        self.color_threshold = 75
        self.pixel_count_threshold = 25000# 100000 # 1080 * 1920 // 10 ####################33 ajustar depen el tamany de la imatge
        self.step = 10 ################## ajustar depen el tamany de la imatge
        self.bridge_object = CvBridge()
        # rospy.loginfo("Before Camera Sub")
        # self.sub = rospy.Subscriber("/camera/image", Image, callback=self.camera_callback)
        self.sub = rospy.Subscriber("/camera/rgb/image_raw", Image, callback=self.camera_callback)
        # rospy.loginfo("After Camera Sub")
        self.pub = rospy.Publisher('integer_topic', Int8, queue_size=1)
   
    def color_distance(self, c1, c2):
    	# return np.abs(np.sum((c1 - c2)))
        return np.sqrt(np.sum((c1 - c2) ** 2))
    
    def check_1_color(self, color_str, pixel):
        return self.color_threshold >= self.color_distance(self.colors[color_str], pixel)

    def check_colors(self):
        c = {color_str: 0 for color_str in self.colors}
        sampled_image = self.image[::self.step, ::self.step]
        for row in sampled_image:
            for pixel in row:
                for color_str in self.colors:
                    # rospy.loginfo(f"Pixel: {pixel}")
                    c[color_str] += self.step*self.step*self.check_1_color(color_str, pixel)
        m = max(c, key=c.get)
        self.color = m if c[m] > self.pixel_count_threshold else None # si utilitzem un threshold posat a ma
        # self.color = m if c[m]*10 > self.image.size//3 else None
        rospy.loginfo("")
        rospy.loginfo(f"{c}")
        rospy.loginfo("")

    def camera_callback(self, messages):
        try:
            self.image = self.bridge_object.imgmsg_to_cv2(messages, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)
        # mirem si hi ha algun color que s'assembla
        # rospy.loginfo(f"size {self.image.size, self.image.shape}")
        self.check_colors()
        if self.color:
            rospy.loginfo(f"Found color {self.color} OuO") #, shape {self.image.size, self.image.shape}")
        else:
            rospy.loginfo("No signal color found")
        
        # aqui publicar (o cridar un metode q publiqui) quan ja vagi (missatge personalitzat)
        msg = Int8()
        msg.data = self.map_colors[self.color]
        self.pub.publish(msg)
        
if __name__== "__main__":
    np.random.seed(373)
    rospy.init_node("color_viewer_node")
    color_viewer()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("ROS Interrupt Exception")

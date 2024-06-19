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

        self.colors = {"red":np.array([95, 55, 226]), "green":np.array([50, 181, 91]), "yellow": np.array([36, 161, 183])} #bgr en cv2
        self.map_colors = {None: 0, "red": 1, "green": 2, "yellow": 3}
        self.color_threshold = 80
        self.pixel_count_threshold = 500# 100000 # 1080 * 1920 // 10 ####################33 ajustar depen el tamany de la imatge
        self.step = 2
        self.step_x = 5
        self.step_y = 5 
        self.bridge_object = CvBridge()
        
        # colors for HSV
        # definir a ma###############################
        # self.colors_hsv = {"red":(np.array([150, 170, 150]), np.array([180, 200, 255])), "green": (np.array([30, 170, 150]), np.array([80, 200, 200])), "yellow": (np.array([10, 170, 160]), np.array([40, 190, 230]))}
        
        """for color_str in self.colors:
            col = np.uint8([[self.colors[color_str]]])
            hsv_col = cv2.cvtColor(col,cv2.COLOR_BGR2HSV)
            upper_lim = hsv_col + 5
            lower_lim = hsv_col - 5
            self.colors_hsv[color_str] = (lower_lim, upper_lim)"""
            
        self.sub = rospy.Subscriber("/camera/image", Image, callback=self.camera_callback)
        # self.sub = rospy.Subscriber("/camera/rgb/image_raw", Image, callback=self.camera_callback)

        self.pub = rospy.Publisher('integer_topic', Int8, queue_size=10)
   
    ###################################
    ### methods for BGR colors#########
    ###################################
    def color_distance(self, c1, c2):
    	# return np.abs(np.sum((c1 - c2)))  # funciona millor al quadrat pq si un R, G, B és diferent la dist aumenta
        return np.sqrt(np.sum((c1 - c2) ** 2))
    
    def check_1_color(self, color_str, pixel):
        return self.color_threshold >= self.color_distance(self.colors[color_str], pixel)

    def check_colors(self):
        c = {color_str: 0 for color_str in self.colors}
        # sampled_image = self.image[::self.step, ::self.step]
        sampled_image = self.crop_image()
        for row in sampled_image:
            for pixel in row:
                for color_str in self.colors:
                    # rospy.loginfo(f"Pixel: {pixel}")
                    c[color_str] += self.check_1_color(color_str, pixel)*self.step#*self.step
        m = max(c, key=c.get)
        self.color = m if c[m] > self.pixel_count_threshold else None # si utilitzem un threshold posat a ma

        rospy.loginfo("")
        rospy.loginfo(f"{c}")
        rospy.loginfo("")

    ###################################
    ### methods for HSV colors#########
    ###################################
    def crop_image(self):
        height, width, channels = self.image.shape
        descentre = height // 3
        rows_to_watch = height // 2
        cropped_image = self.image[(height)//2+descentre:(height)//2+(descentre+rows_to_watch), width//5:4*width//5] # podem pillar nomes la meitat amunt o avall tipo el terra o no
        # si = cropped_image[::self.step, ::self.step]
        si = cropped_image #[::self.step_x, ::self.step_y]
        rospy.loginfo(f"{self.image.shape} --> {cropped_image.shape}")
        return si
    def count_pixels(self, img):
        c = {color_str: 0 for color_str in self.colors}
        for color in self.colors_hsv:
            c[color] = np.sum(cv2.inRange(img, self.colors_hsv[color][0], self.colors_hsv[color][1]))# *self.step_x*self.step_y
        
        rospy.loginfo("")
        rospy.loginfo(f"{c}")
        rospy.loginfo("")
        
        return c


    def check_colors_hsv(self):
        
        sampled_image = self.crop_image()
        self.hsv = cv2.cvtColor(sampled_image, cv2.COLOR_BGR2HSV)
        c = self.count_pixels(sampled_image)

        m = max(c, key=c.get)
        self.color = m if c[m] > self.pixel_count_threshold else None



    def camera_callback(self, messages):
        try:
            self.image = self.bridge_object.imgmsg_to_cv2(messages, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)
        
        self.check_colors()
        # self.check_colors_hsv()
        if self.color:
            rospy.loginfo(f"Found color {self.color} OuO") #, shape {self.image.size, self.image.shape}")
        else:
            rospy.loginfo("No signal color found")
        
        msg = Int8()
        msg.data = self.map_colors[self.color]
        self.pub.publish(msg)
        """if self.color == "red":
            rospy.loginfo("detected red, closing eyes for 3 seconds")
            rospy.sleep(3)"""
        
if __name__== "__main__":
    np.random.seed(373)
    rospy.init_node("color_viewer_node")
    color_viewer()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("ROS Interrupt Exception")

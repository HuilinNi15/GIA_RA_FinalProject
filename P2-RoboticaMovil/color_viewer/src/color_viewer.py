#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan, Image
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback
import actionlib
import numpy as np
import cv2
import math

class color_viewer:
    def __init__(self) -> None:
        rospy.loginfo("Started color viewer node")

        self.colors = {"red":np.array([0, 0, 255]), "green":np.array([0, 255, 0]), "blue": np.array([255, 0, 0])}
        self.color_threshold = 100
        self.pixel_count_threshold = 100 ####################33 ajustar depen el tamany de la imatge

        self.sub = rospy.Subscriber("/camera/image", Image, callback=self.camera_callback)  # canviar de LaserScan a Image? (mirar com es diu)
   
    def color_distance(c1, c2):
        return np.sqrt(np.sum((c1 - c2) ** 2))
    
    def check_1_color(self, color_str, pixel):
        return self.color_threshold >= self.color_distance(self.colors[color_str], pixel)

    def check_colors(self):
        c = {color_str: 0 for color_str in self.colors}
        for row in self.image:
            for pixel in row:
                for color_str in self.colors:
                    self.check_1_color(color_str, pixel)

    def camera_callback(self, messages):
        self.image = messages.image
        # mirem si hi ha algun color que s'assembla
        self.check_colors()
        if self.color:
            rospy.loginfo(f"Found color {self.color} UwU")
        self.update_movement()

if __name__== "__main__":
    np.random.seed(373)
    rospy.init_node("color_viewer_node")
    color_viewer()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("ROS Interrupt Exception")

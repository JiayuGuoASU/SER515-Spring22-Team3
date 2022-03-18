#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WriterNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.pub_vel = self.create_publisher(Twist, "/demo/cmd_vel", 10)
        self.sub_vel = self.create_subscription(LaserScan, "/scan", self.callback , 10);
        self.msg=Twist();
        self.msg.linear.x=0.2;
        self.msg.angular.z=0.0;
        self.pub_vel.publish(self.msg)
        self.time=0
        self.timer=self.create_timer(1, self.timer_callback)
    def timer_callback(self):
        if (self.time>0):
            self.time=self.time-1
    def callback(self, msg):
        if (self.time>0):
            return
        print(msg.ranges[0]);
        msg2=Twist()
        msg2.linear.x=0.2
        msg2.angular.z=0.0;
        minright=min(msg.ranges[0:45])
        minleft=min(msg.ranges[315:360])
        if minright<0.5 and minleft<0.5:
            self.time=5
            msg2.linear.x=-0.1
            msg2.angular.z=0.5
            self.pub_vel.publish(msg2)
            print("both")
            return
        if minleft<0.5:
            print('turn left')
            self.time=5
            msg2.linear.x=-0.1
            msg2.angular.z=0.5      
        if minright<0.5:
            print('turn right')
            self.time=5
            msg2.linear.x=-0.1
            msg2.angular.z=0.5      
        if minright<0.5:
            self.time=5
            msg2.linear.x=-0.1
            msg2.angular.z=-0.5 
        self.pub_vel.publish(msg2)
    def __del__(self):
        msg2=Twist()
        msg2.linear.x=0.0
        msg2.angular.z=0.0;
        self.pub_vel.publish(msg2)

def main(args=None):
    rclpy.init(args=args)
    node = WriterNode("laserScanAndRotate2")
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
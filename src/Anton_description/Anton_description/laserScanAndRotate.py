#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WriterNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.pub_vel = self.create_publisher(Twist, "/cmd_vel", 10)
        self.sub_vel = self.create_subscription(LaserScan, "/scan", self.callback , 10);
        self.msg=Twist();
        self.msg.linear.x=0.2;
        self.msg.angular.z=0.0;
        self.pub_vel.publish(self.msg)
    def callback(self, msg):
        print(msg.ranges[0]);
        msg2=Twist()
        msg2.linear.x=0.2
        msg2.angular.z=0.0;
        if min(msg.ranges[0:45])<0.4 or min(msg.ranges[315:360])<0.4:
            msg2.linear.x=-0.1
            msg2.angular.z=0.5
        self.pub_vel.publish(msg2)
    def __del__(self):
        msg2=Twist()
        msg2.linear.x=0.0
        msg2.angular.z=0.0;
        self.pub_vel.publish(msg2)

def main(args=None):
    rclpy.init(args=args)
    node = WriterNode("laserScanAndRotate")
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class WriterNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.pub_vel = self.create_publisher(Twist, "/demo/cmd_vel", 10)

        self.i = 0
        timer_period = 5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        if self.i % 4 == 0:
            msg.linear.x = 0.2
            msg.linear.z = 0.0
        if self.i % 4 == 1:
            msg.linear.x = 0.0
            msg.linear.z = 0.2
        if self.i % 4 == 2:
            msg.linear.x = -0.2
            msg.linear.z = 0.0
        if self.i % 4 == 3:
            msg.linear.x = 0.0
            msg.linear.z = 0.2
        self.pub_vel.publish(msg)
        # self.get_logger().info("Linearx:%f, Linearz:%f" % (msg.linear.x,msg.linear.z))
        self.i += 1
        self.i = self.i % 4


def main(args=None):
    rclpy.init(args=args)
    node = WriterNode("autoControlNode")
    rclpy.spin(node)
    rclpy.shutdown()

import threading
import rclpy
import os

from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

NODE_NAME = "manullay_cmd_vel_publisher"


def handle_keyboard(publisher):
    while True:
        print('\n- Simple Publisher Menu -')
        print('Press w Command (Move forward)')
        print('Press a Command (Turn Left)')
        print('Press s Command (Move backward)')
        print('Press d Command (Turn Right)')
        print('Press q Command (Stop the robot)')
        print('Press e To Exit')

        menu = input('Input the menu: ')
        msg = Twist()
        if menu == 'w':
            msg.linear.x = 0.2
            msg.angular.z = 0.0
            publisher.publish(msg)
            print(" \n>>> command is published : w")

        elif menu == 's':
            msg.linear.x = -0.2
            msg.angular.z = 0.0
            publisher.publish(msg)
            print(" \n>>> command is published : s")
        elif menu == 'a':
            msg.linear.x = 0.0
            msg.angular.z = 0.4
            publisher.publish(msg)
            print(" \n>>> command is published : s")
        elif menu == 'd':
            msg.linear.x = 0.0
            msg.angular.z = -0.4
            publisher.publish(msg)
            print(" \n>>> command is published : d")
        elif menu == 'q':
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            publisher.publish(msg)
            print(" \n>>> command is published : q")

        elif menu == 'e':
            rclpy.shutdown()
            os._exit(1)


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node(NODE_NAME)
    publisher = node.create_publisher(Twist, "/demo/cmd_vel", 10)

    th = threading.Thread(target=handle_keyboard, args=(publisher,))
    th.start()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

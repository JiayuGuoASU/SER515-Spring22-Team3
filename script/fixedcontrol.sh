#!/bin/bash
ros2 topic pub --once /demo/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -0.1, y: 0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -0.0}}"
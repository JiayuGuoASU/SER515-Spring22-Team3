#!/bin/bash
source /opt/ros/foxy/setup.bash
colcon build
. install/setup.bash
ros2 launch Anton_description display_rviz2.launch.py
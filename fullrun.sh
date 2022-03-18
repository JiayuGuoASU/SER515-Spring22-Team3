#!/bin/bash
echo "fullrun.sh"
source /opt/ros/foxy/setup.bash
cd SER515-Spring22-Team3/
colcon build
. install/setup.bash
ros2 launch Anton_description display_rviz2.launch.py
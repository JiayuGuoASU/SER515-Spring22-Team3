# SER515_GROUP3
1.Installing ROS 2 on Ubuntu Linux
https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Binary.html

# How to Run?
- clone the rep

- new a terminal and input commands below
```
source /opt/ros/foxy/setup.bash
cd SER515-Spring22-Team3/
colcon build
. install/setup.bash
ros2 launch Anton_description display_rviz2.launch.py

new terminal for robot control manually
ros2 topic pub --once /demo/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -0.1, y: 0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -0.0}}"

new terminal for robot control auntomatically
ros2 run Anton_description autoControl
```
# Anton

## Introduction
![software](https://user-images.githubusercontent.com/89811597/163657893-6e2dd8bc-761b-48b7-b6fc-acc3bdb44d29.png)

The Autonomous Rover Development Environment (Anton) simulates an autonomous rover traversing through an unknown 2D environment for discovery and exploration. The rover is equipped with different sensors that help it map and discover the unexplored environment. Human exploration of unexplored areas is sometimes really difficult and is usually dangerous. The hard to reach areas can be extremely fragile and hence not suitable for exploration by a human. Our autonomous rover solves this problem by mapping the hidden areas using LiDAR and other sensors and makes human exploration possible while being either manually or autonomously operated. Hence this project would substantially improve the area of exploration of the unexplored environments and thereby will be beneficial to organizations that use it for their exploration all while keeping the user safe and sound away from structurally compromised locations.

### Overview of our software:
Platform: Our software is building on ROS2, using RVIZ and Gazebo to simulate the robot.

GUI: We have a handy GUI interface for users to interact with the software.

Robot: Our software assembles a robot with multiple configuration files(by user selection).

Map: Our software provides 3 environments for user to choose: RobotCupField, GasStation and Museum.

Mapping System: We use the slam-tool-box to render the map.

Control System: Manually & Automatically control.

Design Pattern: We use design patterns to make our software more flexible and stable.
### What are the advantages/features?
A User-friendly User Interface including the following features: 

- Robot customization:
  - Wheels
  - Casters
  - Chassis
- Map customization
  - Selection from 3 fixed map
- Algorithms selection
  - Manually control
  - Automatically control 
- mapping system
  - Start mapping
  - Saving maps

## What our system looks like:

![design](https://user-images.githubusercontent.com/89811597/163655268-fcc63942-5e20-4d38-af66-1957812b17e3.png)

## Resources of our project

Installation:

User manual:

Demo:https://www.youtube.com/watch?v=1vAm6UHpxhE&list=PLhMbliC9pvicBXlBxUncF8XLzbFfkGw66&ab_channel=ShengdongChen

Taiga Link:https://tree.taiga.io/project/guitang-ser515_group3/timeline

Google Drive:https://drive.google.com/drive/folders/0AN6xGqfHp00kUk9PVA

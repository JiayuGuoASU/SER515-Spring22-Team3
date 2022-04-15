# Anton(Rover)

Demo:https://www.youtube.com/channel/UCQLYQkLfToPyjbYGML2pBFg

Taiga Link:https://tree.taiga.io/project/guitang-ser515_group3/timeline

Google Drive:https://drive.google.com/drive/folders/0AN6xGqfHp00kUk9PVA

# How to Run?

## Linux

Ubuntu 20.04

1.Installing ROS 2 on Ubuntu Linux 

https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Binary.html

2.Clone the repo

3.run install.sh

4.new a terminal and input commands below

```
python3 App.py
```



## Windows

1.Download VScode

2.Download docker

3.Clone the repo

4.Open the repo by using VScode

5.click the "reopen in the Docker" button

6.New a terminal and input commands below

```
python3 App.py
```



## MacOS

1.Download VScode

2.Download docker

3.Clone the repo

4.Open the repo by using VScode

5.click the "reopen in the Docker" button

6.New a terminal and input commands below

```
colcon build
. install/setup.bash
ros2 launch Anton_description display_rviz2.launch.py
```

7.new terminal for robot control auntomatically

```
ros2 run Anton_description autoControl
```


ros2 launch Anton_mapping slam.launch.py
ros2 launch nav2_bringup navigation_launch.py

Saving Map:
ros2 run nav2_map_server map_saver_cli -f ./src/map

8.new terminal for robot manuallly control

```
ros2 run Anton_description mC
```


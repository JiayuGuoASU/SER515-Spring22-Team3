#!/bin/bash
echo "authorize GPG key with apt"
sudo apt update && sudo apt install curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "add the repository to your sources list:"
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
echo "unpack ROS2 packages"
mkdir -p ~/ros2_foxy
cd ~/ros2_foxy
tar xf ~/Downloads/ros2-foxy-20220208-linux-focal-arm64.tar.bz2
echo "Installing and initializing rosdep"
sudo apt update
sudo apt install -y python3-rosdep
sudo rosdep init
rosdep update
echo "Installing the missing dependencies"
rosdep install --from-paths ~/ros2_foxy/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastrtps rti-connext-dds-5.3.1 urdfdom_headers"
echo "Installing the python3 libraries"
sudo apt install -y libpython3-dev python3-pip
pip3 install -U argcomplete
echo "Sourcing the setup script"
echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
echo "Installing packages for URDF"
sudo apt install ros-foxy-joint-state-publisher-gui
sudo apt install ros-foxy-xacro
echo "Installing Colcon"
sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install python3-colcon-common-extensions
echo "Installing Slam Tools"
sudo apt install ros-foxy-slam-toolbox
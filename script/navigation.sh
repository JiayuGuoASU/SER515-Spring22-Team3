#!/bin/bash
echo "automatic.sh"
cd ..
. install/setup.bash
ros2 launch Anton_mapping slam.launch.py
#!/bin/bash
echo "Automatic.sh"
cd ..
. install/setup.bash
ros2 run Anton_description lmC

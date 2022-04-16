echo "downloadmap.sh"
cd ..
. install/setup.bash
ros2 run nav2_map_server map_saver_cli -f ~/map --ros-args -p save_map_timeout:=10000
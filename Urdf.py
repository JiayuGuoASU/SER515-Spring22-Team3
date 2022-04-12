import xacro
import os

# package_name = 'Anton_description'
# urdf_name = 'roverTest.urdf'
# rviz_configuration_name = 'urdf_config.rviz'
# pkg_share = launch_ros.substitutions.FindPackageShare(package= package_name).find(package_name)
# default_model_path = os.path.join(pkg_share, f'urdf/{urdf_name}')
# default_rviz_config_path = os.path.join(pkg_share, f'rviz/{rviz_configuration_name}')
# world_path = os.path.join(pkg_share, 'world/modelTest.sdf'),

xacro_file = "./src/Anton_description/urdf/xacro/Anton.xacro"
assert os.path.exists(xacro_file), "The box_bot.xacro doesnt exist in "+str(xacro_file)

robot_description_config = xacro.process_file(xacro_file)
robot_desc = robot_description_config.toxml()
print(robot_desc)

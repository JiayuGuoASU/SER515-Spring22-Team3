import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
import xacro

# Reference: https://navigation.ros.org/setup_guides/urdf/setup_urdf.html

def generate_launch_description():
    package_name = 'Anton_description'
    urdf_name = 'Anton.urdf'
    rviz_configuration_name = 'urdf_config.rviz'
    pkg_share = launch_ros.substitutions.FindPackageShare(package= package_name).find(package_name)
    default_model_path = os.path.join(pkg_share, f'urdf/{urdf_name}')
    default_rviz_config_path = os.path.join(pkg_share, f'rviz/{rviz_configuration_name}')
    world_path=os.path.join(pkg_share, 'world/cafe.sdf'),

    # assert os.path.exists(default_model_path), "The box_bot.xacro doesnt exist in "+str(default_model_path)
    # robot_description_config = xacro.process_file(default_model_path)
    # robot_desc = robot_description_config.toxml()
    # print(robot_desc)

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
    )
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=launch.conditions.UnlessCondition(LaunchConfiguration('gui'))
    )

    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )
    spawn_entity = launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'Anton', '-topic', 'robot_description'],
        output='screen'
    )

    robot_localization_node = launch_ros.actions.Node(
       package='robot_localization',
       executable='ekf_node',
       name='ekf_filter_node',
       output='screen',
       parameters=[os.path.join(pkg_share, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
)

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='gui', default_value='True',
                                            description='Flag to enable joint_state_publisher_gui'),
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                            description='Absolute path to rviz config file'),
        launch.actions.ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path], output='screen'),
        launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='True',
                                            description='Flag to enable use_sim_time'),
        joint_state_publisher_node,
        robot_state_publisher_node,
        spawn_entity,
        robot_localization_node,
        rviz_node
    ])
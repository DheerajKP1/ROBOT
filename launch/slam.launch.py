import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name='mtp_robot'
    # Get the path to your configuration file
    config_dir = os.path.join(get_package_share_directory(package_name), 'config')
    slam_params_file = os.path.join(config_dir, 'mapper_params.yaml')

    # SLAM Toolbox Node
    start_async_slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[slam_params_file],
        remappings=[('/scan', '/scan'), # Explicitly remap if needed
                    ('/tf', 'tf'),
                    ('/tf_static', 'tf_static')]
    )

    # RViz Node for visualization
    start_rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', os.path.join(get_package_share_directory(package_name), 'rviz', 'slam.rviz')],
        output='screen'
    )
    
    ld = LaunchDescription()

    ld.add_action(start_async_slam_toolbox_node)
    ld.add_action(start_rviz_node)

    return ld
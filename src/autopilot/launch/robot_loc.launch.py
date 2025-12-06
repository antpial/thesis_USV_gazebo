from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import TimerAction
import os

def generate_launch_description():
    pkg_name = 'autopilot'

    # Ścieżki do plików konfiguracyjnych
    ekf_config_path = PathJoinSubstitution([FindPackageShare(pkg_name), 'config', 'ekf.yaml'])
    navsat_config_path = PathJoinSubstitution([FindPackageShare(pkg_name), 'config', 'navsat.yaml'])

    # Debug: możesz odkomentować, jeśli chcesz sprawdzić, czy pliki istnieją
    # pkg_share = FindPackageShare(pkg_name).find(pkg_name)
    # print(f"Package share directory: {pkg_share}")
    # print(f"EKF config path exists: {os.path.isfile(os.path.join(pkg_share, 'config', 'ekf.yaml'))}")
    # print(f"NavSat config path exists: {os.path.isfile(os.path.join(pkg_share, 'config', 'navsat.yaml'))}")

    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0.1', '0', '0', '0', 'base_link', 'gps_link'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0.2', '0', '0', '0', '0', 'base_link', 'imu_link'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0.0', '0.5', '0', '0', '0', 'base_link', 'magnetometer_link'],
        ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=['0','0','0','0','0','0','odom','base_link'],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
        # ),
        Node(
            package='ros_gz_bridge_custom',
            executable='bridge_node',
            name='ros_gz_bridge_node',
            output='screen',
        ),
        Node(
            package='autopilot',
            executable='compass',
            name='CompassOdomNode',
            output='screen',
        ),
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_config_path]
        ),
        TimerAction(
            period=5.0,  # 1 sekunda opóźnienia
            actions=[
                Node(
                    package='robot_localization',
                    executable='navsat_transform_node',
                    name='navsat_transform_node',
                    output='screen',
                    parameters=[navsat_config_path]
                )
            ]
        )
    ])

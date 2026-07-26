import os
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    urdf_path = PathJoinSubstitution([
        FindPackageShare("robo"),
        "urdf",
        "robot.urdf"
    ])
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
            'robot_description': ParameterValue(urdf_path, value_type=str)
        }]
    )
    spawn_entity_node = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            '-name', 'simple_robot',
            '-topic', 'robot_description',
            '-z', '0.5'
        ],
        output='screen'
    )
    bridge_node = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist",
            "/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry",
            "/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image"
        ],
        output="screen"
    )

    return LaunchDescription([
        robot_state_publisher_node,
        spawn_entity_node,
        bridge_node
    ])
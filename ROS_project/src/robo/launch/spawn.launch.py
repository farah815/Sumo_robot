import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
       pkg_share = get_package_share_directory('robo')
    urdf_file = os.path.join(pkg_share, 'urdf', 'robot.urdf')

    with open(urdf_file, 'r') as infp:
        robot_description_content = infp.read()

    
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description_content
        }]
    )

   
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'simple_robot',
            '-topic', 'robot_description',
            '-z', '0.3'
        ],
        output='screen'
    )

    
    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
            '/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image'
        ],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        spawn_robot,
        bridge_node
    ])

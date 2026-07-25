import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    # 1. تحديد اسم الباكدج ومسار ملف الـ URDF
    pkg_name = 'sumo_description'
    urdf_file = os.path.join(get_package_share_directory(pkg_name), 'urdf', 'sumo.urdf.xacro')

    # 2. ترجمة ملف الـ Xacro لـ URDF يفهمه النظام
    robot_description = {'robot_description': Command(['xacro ', urdf_file])}

    # 3. نود الـ Robot State Publisher (ده العقل اللي بيبعت تفاصيل الروبوت للمحاكاة)
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    # 4. نود الـ Joint State Publisher GUI (ده اللي هيفتحلك شاشة البكرات عشان تحركي المفاصل بالماوس)
    node_joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    # 5. نود الـ RViz (برنامج العرض الـ 3D نفسه)
    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        node_robot_state_publisher,
        node_joint_state_publisher_gui,
        node_rviz
    ])
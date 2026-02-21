from launch import LaunchDescription
from launch_ros.actions import Node

"""
TODO: Complete this launch file to:
1. Launch the 'talker' node from package 'ros2_launch_demo' with:
   - Parameter 'message_prefix' set to 'ROS2'
2. Launch the 'listener' node from package 'ros2_launch_demo'

Hint: Use Node() action with:
- package='ros2_launch_demo'
- executable='talker' or 'listener'
- parameters=[{'message_prefix': 'ROS2'}] for talker
"""


def generate_launch_description():
    return LaunchDescription(
        [
	Node(
            package='ros2_launch_demo',
            executable='talker',
            name='talker'
        ),
        Node(
            package='ros2_launch_demo',
            executable='listener',
            name='listener'
        ),
            # TODO: Add talker node with message_prefix parameter
            # TODO: Add listener node
        ]
    )

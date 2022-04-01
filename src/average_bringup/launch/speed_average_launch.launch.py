from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    speed_publisher_node = Node(
        package = "sensors",
        executable = "publisher_speed_node"
    )

    speed_averageCalc_node = Node(
        package = "data_processor",
        executable = "speed_subscriber"
    )

    ld.add_action(speed_publisher_node)
    ld.add_action(speed_averageCalc_node)

    return ld
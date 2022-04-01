from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    temp_publisher_node = Node(
        package = "sensors",
        executable = "publisher_temp_node"
    )

    temp_averageCalc_node = Node(
        package = "data_processor",
        executable = "temp_subscriber"
    )

    ld.add_action(temp_publisher_node)
    ld.add_action(temp_averageCalc_node)

    return ld
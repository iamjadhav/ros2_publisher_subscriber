from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    laser_publisher_node = Node(
        package = "sensors",
        executable = "publisher_laser_node"
    )

    laser_averageCalc_node = Node(
        package = "data_processor",
        executable = "laser_subscriber"
    )

    ld.add_action(laser_publisher_node)
    ld.add_action(laser_averageCalc_node)

    return ld
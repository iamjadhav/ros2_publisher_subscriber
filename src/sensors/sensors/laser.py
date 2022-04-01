#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64
import random

# SensorTwoNode Class which publishes random Distance data between 0 to 20 
# Meters on the "laser_data" topic at the rate of 80Hz.
class SensorThreeNode(Node):

    def __init__(self):
        super().__init__("laser_sensor")
        self.publisher_ =  self.create_publisher(Float64, "laser_data", 20)
        self.timer = self.create_timer(0.0125, self.publish_data)
        self.get_logger().info(" Laser Data Transmission Initiated ! ")

    def publish_data(self):
        msg = Float64()
        value = round(random.uniform(0, 20), 2)
        msg.data = value
        self.publisher_.publish(msg)


def main(args = None):
    rclpy.init(args = args)
    node = SensorThreeNode()   
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__== "__main__":
    main()
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64
import random

# SensorOneNode Class which publishes random Temperature data between 60 to 85 
# degrees fahrenheit on the "temp_data" topic at the rate of 30Hz.
class SensorOneNode(Node):

    def __init__(self):
        super().__init__("temp_sensor")
        self.publisher_ =  self.create_publisher(Float64, "temp_data", 20)
        self.timer = self.create_timer(0.0333, self.publish_data)
        self.get_logger().info(" Temperature Data Transmission Initiated ! ")

    def publish_data(self):
        msg = Float64()
        value = round(random.uniform(60, 85), 2)
        msg.data = value
        self.publisher_.publish(msg)


def main(args = None):
    rclpy.init(args = args)
    node = SensorOneNode()    
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__== "__main__":
    main()
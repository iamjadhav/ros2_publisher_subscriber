#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from random import randint

# SensorTwoNode Class which publishes random Speed data between 50 to 80 
# Mph on the "speed_data" topic at the rate of 35Hz.
class SensorTwoNode(Node):

    def __init__(self):
        super().__init__("speed_sensor")
        self.publisher_ =  self.create_publisher(Int64, "speed_data", 20)
        self.timer = self.create_timer(0.0285, self.publish_data)
        self.get_logger().info(" Speed Data Transmission Initiated ! ")

    def publish_data(self):
        msg = Int64()
        value = randint(50, 80)
        msg.data = value
        self.publisher_.publish(msg)


def main(args = None):
    rclpy.init(args = args)
    node = SensorTwoNode()  
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__== "__main__":
    main()
#!/usr/bin/env python3

from numpy import float64
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64

# Laser Data Subscriber Class which also publishes Distance Average 
# on the "average_distance" topic.
class LaserSubscriber(Node):

    def __init__(self):
        super().__init__("laser_subscriber")
        self.average_list = []
        self.ave = 0

        # Laser Data Subscriber
        self.subscriber_ = self.create_subscription(
            Float64, "laser_data", self.callback_laser_data, 20)
        self.get_logger().info(" Laser Subscriber Initiated! ")
                
        # Distance Average Publisher
        self.publisher_ =  self.create_publisher(Float64, "average_distance", 20)
        self.get_logger().info(" Distance Average Published! ")

        self.subscriber_

    def publish_data(self):
        msg = Float64()
        msg.data = float64(self.ave)
        self.publisher_.publish(msg)

    def callback_laser_data(self, msg):

        # Storing 20 entries
        for i in range(20):
            self.average_list.append(msg.data)

        # Publishing Average    
        self.ave = self.calc_average()
        self.timer = self.create_timer(0.5, self.publish_data)
        self.average_list.clear()
        self.get_logger().info('Average Distance is : "%s" Meters' % self.ave)

    # Calculating Average
    def calc_average(self):
        self.ave = sum(self.average_list) / len(self.average_list)
        return round(self.ave, 2)


def main(args = None):
    rclpy.init(args = args)
    node = LaserSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

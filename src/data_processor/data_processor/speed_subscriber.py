#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

# Speed Data Subscriber Class which also publishes Speed Average 
# on the "average_speed" topic.
class SpeedSubscriber(Node):

    def __init__(self):
        super().__init__("speed_subscriber")
        self.average_list = []
        self.ave = 0

        # Speed Data Subscriber       
        self.subscriber_ = self.create_subscription(
            Int64, "speed_data", self.callback_speed_data, 20)
        self.get_logger().info(" Speed Subscriber Initiated! ")
                
        # Speed Average Publisher
        self.publisher_ =  self.create_publisher(Int64, "average_speed", 20)
        self.get_logger().info(" Speed Average Published! ")

        self.subscriber_

    def publish_data(self):
        msg = Int64()
        msg.data = int(self.ave)
        self.publisher_.publish(msg)

    def callback_speed_data(self, msg):
        
        # Storing 20 entries
        for i in range(20):
            self.average_list.append(msg.data)

        # Publishing Average    
        self.ave = self.calc_average()
        self.timer = self.create_timer(0.5, self.publish_data)
        self.average_list.clear()
        self.get_logger().info('Average Speed is : "%s" Mph' % self.ave)

    # Calculating Average
    def calc_average(self):
        self.ave = sum(self.average_list) / len(self.average_list)
        return self.ave


def main(args = None):
    rclpy.init(args = args)
    node = SpeedSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

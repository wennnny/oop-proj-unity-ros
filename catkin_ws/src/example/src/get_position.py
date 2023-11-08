#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import String

class GetPosition:
    def __init__(self):
        self.position_sub = rospy.Subscriber('/cube_position', Float64MultiArray, self.callback) # define a subscriber to receive position data from unity to python (if data comes will automatically call callback function)
        self.position_string_pub = rospy.Publisher('/get_position', String, queue_size=3) # define a publisher tosend position data from python to unity

    def callback(self, msg):
        x = round(msg.data[0], 5)
        y = round(msg.data[1], 5)
        self.position_string_pub.publish(f"position: ("+ str(x) + ", " + str(y) + ")")

if __name__ == "__main__":
    rospy.init_node('get_position_node')
    get_position = GetPosition()
    rospy.spin()
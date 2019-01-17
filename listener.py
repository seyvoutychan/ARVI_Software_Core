#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    if str(data.data) == "1.0":
        rospy.loginfo("You turned on the LED %s", data.data)
    elif str(data.data) == "0.0":
        rospy.loginfo("You turned off the LED %s", data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()

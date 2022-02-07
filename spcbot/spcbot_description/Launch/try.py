#! usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
from lol import assign
rospy.init_node('obiwan')
rate=rospy.Rate(2)
pub=rospy.Publisher('/counter',Int32,queue_size=1)
while not rospy.is_shutdown():
    pub.publish(5)
    rate.sleep()
    
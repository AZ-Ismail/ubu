
#! usr/bin/env python

import rospy
class assign:
    def __init__(self,topic,msg,nbr):
        self.topic=topic
        self.msg=msg
        self.nbr=nbr
    def pubbb(self):
        pub=rospy.Publisher(self.topic,self.msg,queue_size=1)
        pub.publish(self.nbr)
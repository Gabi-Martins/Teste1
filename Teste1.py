import rospy
from std_msgs.msg import String
import math

rospy.init_node('test1')

def timerCallBack(event):
    msg = String()
    msg.data = '2017016681'
    pub.publish(msg)
    
pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()

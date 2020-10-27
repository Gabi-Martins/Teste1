import rospy
from std_msgs.msg import String
import math

rospy.init_node('Teste2')

matricula = '0'

def pmatricula(mat):
      global matricula
      matricula=mat.data

sub = rospy.Subscriber('/topic1', String, pmatricula)

def timerCallBack(event):
    soma = 0
    for digit in matricula:
        soma += int(digit)
    msg=String()
    msg.data = str(soma)
    pub.publish(msg)
    
pub = rospy.Publisher('/topic2', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()
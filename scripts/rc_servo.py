#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import time
import Adafruit_PCA9685

def recv_joystick(data):
    rospy.loginfo(type(data))
    rospy.loginfo(data.data)

class App:

    def __init__(self):
        pass

    def update_pan(self, angle):
        duty = int( float(angle) * 2.17 + 102 )
        pwm.set_pwm(0, 0, duty)

    def update_tilt(self, angle):
        duty = int( float(angle) * 2.17 + 102 )
        pwm.set_pwm(1, 0, duty)

if __name__ == '__main__':
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)
    app = App()
    
    rospy.init_node('servo')
    rospy.Subscriber("servo", UInt16, recv_joystick)
    rospy.spin()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
# メッセージの型等のimport
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import time
import Adafruit_PCA9685

class rc_servo():
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)

        # Subscriberを作成
        self.subscriber = rospy.Subscriber('joy', Joy, self.callback, queue_size=1)

    def callback(self, joy_msg):
        # アナログ左スティック（左側＋、右側ー）
        a =  90*joy_msg.axes[0]/1.3
        pos = 90 +int(a)

        pulse = (650-150)*pos/180+150+(-10)
        #self.pwm.set_pwm(0, 0, pulse)

        rospy.loginfo(joy_msg)

        duty = int( float(pos) * 2.17 + 102 )
        self.pwm.set_pwm(0, 0, duty)
        print "a,duty,button0" , a, duty, joy_msg.buttons[0]

if __name__ == '__main__':
    # nodeの立ち上げ
    rospy.init_node('rc_servo')
    rate = rospy.Rate(10) # 10Hz

    # クラスの作成
    sub = rc_servo()
    rospy.spin()




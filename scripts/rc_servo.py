#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
# メッセージの型等のimport
from geometry_msgs.msg import Twist

import time
import Adafruit_PCA9685

class Subscribers():
    def __init__(self):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)

        # Subscriberを作成
        self.subscriber = rospy.Subscriber('joy', Twist, self.callback)
            # messageの型を作成
        self.message = Twist()

    def callback(self, message):
        # アナログ左スティック（左側＋、右側ー）
        a =  90*message.buttons[0]/1.3
        pos = 90 +int(a)

        pulse = (650-150)*pos/180+150+(-10)
        pwm.set_pwm(0, 0, pulse)

        #duty = int( float(angle) * 2.17 + 102 )
        #pwm.set_pwm(0, 0, duty)

def main():
    # nodeの立ち上げ
    rospy.init_node('rc_servo')

    # クラスの作成
    sub = Subscribers()
    rospy.spin()

if __name__ == '__main__':
   main()



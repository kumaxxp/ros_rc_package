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
        pwm.set_pwm_freq(50)

        # Subscriberを作成
        self.subscriber = rospy.Subscriber('/rc_servo', Twist, self.callback)
            # messageの型を作成
        self.message = Twist()

    def callback(self, message):
        # callback時の処理(sendが必要な場合はここにsendを入れるやるのもあり)
        duty = int( float(angle) * 2.17 + 102 )
        pwm.set_pwm(0, 0, duty)

def main():
    # nodeの立ち上げ
    rospy.init_node('rc_servo')

    # クラスの作成
    sub = Subscribers()

if __name__ == '__main__':
   main()



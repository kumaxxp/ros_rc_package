import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('joy', Joy, self.joy_callback, queue_size=1)
        self._twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
        self.operation = [0.0, 0.0, 0.0]

    def joy_callback(self, joy_msg):
        self.operation[0] = joy_msg.axes[0]
        self.operation[1] = joy_msg.axes[1]

if __name__ == '__main__':
    rospy.init_node('joy_twist')
    rate = rospy.Rate(10) # 10hz
    joy_twist = JoyTwist()
    twist = Twist()
    
    while not rospy.is_shutdown():
        twist.linear.x = joy_twist.operation[1]
        twist.angular.z = joy_twist.operation[0]
        rospy.loginfo(twist)
        joy_twist._twist_pub.publish(twist)
        rate.sleep()
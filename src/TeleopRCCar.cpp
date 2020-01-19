// TeleopRCCar.cpp

#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/Joy.h>

class TeleopRCCar
{
    public:
    TeleopRCCar();

    private:
    void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);

    ros::NodeHandle m_nh;
    ros::Publisher  m_pub;
    ros::Subscriber m_sub;
};

TeleopRCCar::TeleopRCCar()
{
    m_pub = m_nh.advertise<geometry_msgs::Twist>("cmd_vel", 1);
    m_sub = m_nh.subscribe<sensor_msgs::Joy>("joy", 10, &TeleopRCCar::joyCallback, this);
}

void TeleopRCCar::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
    double dScale = 1;

    geometry_msgs::Twist twist;
    twist.angular.x = dScale*joy->axes[0];
    twist.linear.x = dScale*joy->axes[1];
    m_pub.publish(twist);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "Teleop_rccar");
    TeleopRCCar teleop_rccar;

    ros::spin();
}
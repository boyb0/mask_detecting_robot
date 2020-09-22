#!/usr/bin/env python

# Импортирање на модули
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


# Глобални променливи
cmd = ""


def callback(cmd_msg):
    global cmd

    cmd = cmd_msg.data


def actuators_node():
    global cmd
    # Иницијализација на јазолот
    rospy.init_node('actuators_node')
    pub = rospy.Publisher("/RosAria/cmd_vel", Twist, queue_size=5)
    rospy.Subscriber("actuators_cmd", String, callback)
    rate = rospy.Rate(20)

    # Се'додека програмата на роботот не е прекината, се читаат командите за на која страна треба да се ротира роботот,
    # се конвертираат во ROS порака и се испраќаат до следниот јазол
    while not rospy.is_shutdown():
        rospy.loginfo(cmd)

        if cmd == "Right":
            # Ротирај го роботот на десно
            linear = Vector3(x=0.0, y=0.0, z=0.0)
            angular = Vector3(x=0.0, y=0.0, z=-0.2)
        elif cmd == "Left":
            # Ротирај го роботот на лево
            linear = Vector3(x=0.0, y=0.0, z=0.0)
            angular = Vector3(x=0.0, y=0.0, z=0.2)
        elif cmd == "Forward":
            # Движи го роботот напред
            linear = Vector3(x=0.125, y=0.0, z=0.0)
            angular = Vector3(x=0.0, y=0.0, z=0.0)
        elif cmd == "Backwards":
            # Ротирај целосно на десно се дур не се сврти роботот за 180 степени
            linear = Vector3(x=0.0, y=0.0, z=0.0)
            angular = Vector3(x=0.0, y=0.0, z=-0.2)
        else:
            # Стопирај го роботот
            linear = Vector3(x=0.0, y=0.0, z=0.0)
            angular = Vector3(x=0.0, y=0.0, z=0.0)

        twist = Twist(linear=linear, angular=angular)
        pub.publish(twist)

        rate.sleep()


if __name__ == "__main__":
    actuators_node()

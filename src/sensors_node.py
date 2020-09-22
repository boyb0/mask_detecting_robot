#!/usr/bin/env python

# Импортирање на модули
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud

# Глобални променливи
pub = rospy.Publisher('sensor_data', String, queue_size=5)

# Функција преку која се мери растојанието до некоја препрека преку сите сензори
def get_distances(points):
    s0 = points[0].x + points[0].y
    s1 = points[1].x + points[1].y
    s2 = points[2].x + points[2].y
    s3 = points[3].x + points[3].y
    s4 = points[4].x + abs(points[4].y)
    s5 = points[5].x + abs(points[5].y)
    s6 = points[6].x + abs(points[6].y)
    s7 = points[7].x + abs(points[7].y)

    return s0, s1, s2, s3, s4, s5, s6, s7


def callback(sensor_data_msg):
    global pub
    # Превземи го растојанието од сензорот до некоја препрека за сите 8 сензори
    s0, s1, s2, s3, s4, s5, s6, s7 = get_distances(sensor_data_msg.points)

    rospy.loginfo("Sensor 0: "+ str(s0))
    rospy.loginfo("Sensor 1: "+ str(s1))
    rospy.loginfo("Sensor 2: "+ str(s2))
    rospy.loginfo("Sensor 3: "+ str(s3))
    rospy.loginfo("Sensor 4: "+ str(s4))
    rospy.loginfo("Sensor 5: "+ str(s5))
    rospy.loginfo("Sensor 6: "+ str(s6))
    rospy.loginfo("Sensor 7: "+ str(s7))

    # s3 и s4 се двата средни сензори, додека s0 е крајниот лев сензор и s7 е крајниот десен сензор
    if s3 < 0.80 or s4 < 0.80:
        # Пречки кои се наоѓаат пред роботот, десно и лево од него, односно мртва точка
        if s0 < 0.80 and s7 < 0.80: 
            pub.publish(String("Dead end"))
        # Пречки кои се наоѓаат пред роботот и лево од него
        elif s0 < 0.65:
            pub.publish(String("Left"))
        # Пречки кои се наоѓаат пред роботот и десно од него
        elif s7 < 0.65:
            pub.publish(String("Right"))
        # Пречки кои се наоѓаат само пред роботот
        else:
            pub.publish(String("Front"))
    # Нема пречки
    else:
        pub.publish(String("None"))


def sensors_node():
    # Иницијализација на јазолот
    rospy.init_node('sensors_node')
    rospy.Subscriber("/RosAria/sonar", PointCloud, callback)
    # Оневозможува завршување на јазолот се дур истиот не се изгаси 'рачно'
    rospy.spin()


if __name__ == "__main__":
    sensors_node()

#!/usr/bin/env python

# Модул за работа со робот
import rospy
# Останати модули
import cv2

# Модул за размена на пораки меѓу јазлите
from sensor_msgs.msg import Image
# Модул кој овозможува работенје со OpenCV функции врз фрејмовите прочитани од камерата
from cv_bridge import CvBridge, CvBridgeError

# Глобални променливи
bridge = CvBridge()


def callback(img_msg):
    global bridge
    img = None

    # Конверзија на сензорната порака во OpenCV формат
    try:
        img = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # Прикажување на фрејм
    cv2.imshow("CAMERA01", img)
    cv2.waitKey(10)


def video_display_node():
    # Иницијализација на јазолот
    rospy.init_node('video_display_node')
    rospy.Subscriber("frame", Image, callback)

    # Оневозможува завршување на јазолот се дур истиот не се изгаси 'рачно'
    rospy.spin()


if __name__ == "__main__":
    video_display_node()

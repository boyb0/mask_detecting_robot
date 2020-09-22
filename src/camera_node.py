#!/usr/bin/env python

# Модул за работа со робот
import rospy
# Останати модули
import time

# Модул за размена на пораки кои доаѓаат од сензорите (камера во моментов)
from sensor_msgs.msg import Image
# Модул кој овозможува работење со OpenCV функционалности врз фрејмовите прочитани од камерата
from cv_bridge import CvBridge
from imutils.video import VideoStream

# Глобални променливи
bridge = CvBridge()
vs = VideoStream(src=0).start()


def camera_node():
    global bridge
    global vs

    # Иницијализација на јазолот
    rospy.init_node('camera_node')
    pub = rospy.Publisher('frame', Image, queue_size=5)
    rate = rospy.Rate(20)
    time.sleep(2.0)

    # Сe' додека програмата на роботот не е прекината, се читаат фрејмови, се конвертираат во ROS порака
    # и се испраќаат до следниот јазол
    while not rospy.is_shutdown():
        frame = vs.read()
        if frame is not None:
            img_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            pub.publish(img_msg)
        rate.sleep()


if __name__ == "__main__":
    camera_node()

#!/usr/bin/env python

# Импортирање на модули
import rospy
from std_msgs.msg import String
from time import sleep
from my_project.srv import MessageSendingService


# Глобални променливи
move = ""
wait = False
turning = False

# Помошна класа која служи како container
class MyMessage:
    def __init__(self, text):
        self.text = text

# Испраќање на добиената порака до соодветниот сервис за приказ на истата
def send_request_ms(message):
    """
    Sends a request to the message sending service node
    """
    rospy.wait_for_service("message_sending_service")
    try:
        service = rospy.ServiceProxy("message_sending_service", MessageSendingService)

        rospy.loginfo("SENDING MESSAGE...")

        response = service(message)

        if response.sent:
            rospy.loginfo("MESSAGE SENT SUCCESSFULLY!")
    except rospy.ServiceException as e:
        rospy.loginfo("Service access failed: %s" % e)

# Дефинирање на движењето на роботот врз основа на прочитаната информација од сензорите
def sensor_data_callback(sensor_data_msg):
    global move

    obstacle = sensor_data_msg.data

    if obstacle == "Dead end":
        # Доколку има мртва точка, тогаш роботот треба да се сврти за 180 степени на десно
        move = "Backwards"
    elif obstacle == "Left":
        # Доколку има препрека од лево, тогаш роботот треба да се сврти на десно
        move = "Right"
    elif obstacle == "Right":
        # Доколку има препрека од десно, тогаш роботот треба да се сврти на лево
        move = "Left"
    elif obstacle == "None":
        # Доколку нема препрека, роботот си продолжува со движење напред
        move = "Forward"
    elif obstacle == "Front":
        # Доколку има препрека од право, тогаш роботот треба да се сврти на десно
        move = "Left"
    else:
        # Доколку се случи ситуација која не е наведена горе, тогаш роботот треба да застане
        move = "Stop"


def mask_detection_callback(mask_detection_msg):
    global wait
    global turning


    # Проверка дали роботот се врти
    if not turning:

        try:
            # Проверка дали е детектирано барем едно лице
            if mask_detection_msg.data != "0":
                message = mask_detection_msg.data
                wait = True

                # Испечати
                m = MyMessage(message)
                send_request_ms(m)
                # sleep(5)

                wait = False

        except Exception as e:
            pass


def main_node():
    global move
    global wait
    global turning

    # Иницијализација на јазолот
    rospy.init_node('main_node')
    pub = rospy.Publisher("actuators_cmd", String, queue_size=5)
    rospy.Subscriber("sensor_data", String, sensor_data_callback)
    rospy.Subscriber("mask_detection", String, mask_detection_callback)
    rate = rospy.Rate(20)

    # Се' додека програмата на роботот не е прекината, роботот се врти во соодветната насока која е прочитана
    while not rospy.is_shutdown():
        if not wait:
            pub.publish(String(move))

            if move == "Right":
                # Роботот се врти за 90 степени на десно
                turning = True
                sleep(8)
                turning = False
            if move == "Left":
                # Роботот се врти за 90 степени на лево
                turning = True
                sleep(8)
                turning = False
            if move == "Backwards":
                # Роботот се врти за 180 степени на десно
                turning = True
                sleep(16)
                turning = False
        else:
            # Robotot se stopira
            pub.publish(String("Stop"))

        rate.sleep()


if __name__ == "__main__":
    main_node()

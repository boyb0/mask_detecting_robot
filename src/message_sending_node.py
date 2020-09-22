#!/usr/bin/env python

# Импортирање на модули
import rospy
from my_project.srv import MessageSendingService
from my_project.srv import MessageSendingServiceResponse

# Функција која се справува со дојдовната порака од главниот јазол и истата ја печати
def handle_request(data):
    message = data.message

    rospy.loginfo(message.text)

    return MessageSendingServiceResponse(True)


def message_sending_node():
    rospy.init_node('message_sending_node')

    rospy.Service("message_sending_service", MessageSendingService, handle_request)

    rospy.spin()


if __name__ == "__main__":
    message_sending_node()

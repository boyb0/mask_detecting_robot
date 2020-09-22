#!/usr/bin/env python

# Модул за работа со робот
import rospy
# Останати модули
import cv2
import numpy as np
import time
from datetime import datetime

# Модул за работа со пораки меѓу јазлите
from sensor_msgs.msg import Image
from std_msgs.msg import String

# Модул кој овозможува работење со OpenCV функции врз фрејмовите прочитани од камерата
from cv_bridge import CvBridge, CvBridgeError

# Модули кои помагаат во обработката на фрејмовите за детекција на лице и маска
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Глобални променливи
bridge = CvBridge()
cnt = 0
pub = rospy.Publisher("mask_detection", String, queue_size=5)

# Иницијализација на детекторите за лице и маска
# Мора да се наведат АПСОЛУТНИ ПАТЕКИ до детекторите
faceDetect = cv2.dnn.readNet(config="/home/bojan/catkin_ws/src/my_project/model/deploy.prototxt",
                             model="/home/bojan/catkin_ws/src/my_project/model/res10_300x300_ssd_iter_140000.caffemodel")

maskDetect = load_model("/home/bojan/catkin_ws/src/my_project/MaskDetectionModel.model")


def detect_mask(frame):
    global faceDetect
    global maskDetect

    # Вчитување на висината и ширината на сликата
    height = frame.shape[0]
    width = frame.shape[1]

    # Конструкција на блоб (предпроцесирана слика спремна за невронска мрежа)
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300,300), (104.0, 177.0, 123.0))

    # Предавање на блоб на невронската мрежа за детекција на лице
    start = time.time()
    faceDetect.setInput(blob)
    detections = faceDetect.forward()
    end = time.time()

    # Прикажување на информации во врска со времето потребно за извршување на детекција
    rospy.loginfo("Face detection took {:.6f} seconds".format(end - start))

    # Иницијализација на листа од лица, нивни локации на сликата и со колкава веројатност (не)носат маска
    faces = []
    locs = []
    preds = []

    for i in range(0,detections.shape[2]):
        # Превземање на нивото на доверба (веројатноста да е детектиран лик)
        conf = detections[0, 0, i, 2]
        # Споредба на нивото со однапред дефинирана граница со што се овозможува филтрирање на слабо точни детекции
        if conf > 0.5:
            # Пресметување на (x,y) координатите за рамката околу лицето
            box = detections[0, 0, i, 3:7] * np.array([width,height,width,height])
            (x_start, y_start, x_end, y_end) = box.astype("int")

            # Проверка дали рамките влегуваат во димензиите на сликата
            (x_start, y_start) = (max(0, x_start), max(0, y_start))
            (x_end, y_end) = (min(width-1, x_end), min(height-1, y_end))

            # Превземање на ROI на лицето, конверзија од BGR во RGB, промена на димензии во 224 x 224 и предпроцесирање
            face = frame[y_start:y_end, x_start:x_end]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224,224))
            face = img_to_array(face)
            face = preprocess_input(face)

            faces.append(face)
            locs.append((x_start, y_start, x_end, y_end))

    # Предвидување се прави само доколку е детектирано барем едно лице
    if len(faces) >= 1:
        faces = np.array(faces, dtype="float32")
        preds = maskDetect.predict(faces, batch_size=32)

    return (locs,preds)

def callback(img_msg):
    global bridge
    global cnt
    global pub
    cnt_no_mask = 0
    cnt_mask = 0
    mask_detection_msg = "0"
    flag = False

    # Се зема секој 5 фрејм во предвид
    if cnt % 5 == 0:
        current_time = "00:00:00"
        img = None
        try:
            img = bridge.imgmsg_to_cv2(img_msg,"bgr8")

            # Превземање на моменталното време
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            # Детекција на сите лица со соодветните веројатности дали носат маска или не
            (locations, predictions) = detect_mask(img)
        except CvBridgeError as e:
            print(e)

        # Доколку фрејмот е правилно процесиран	
	if img is not None:            
            cnt_no_mask = 0
            cnt_mask = 0
            for (square, predictions) in zip(locations, predictions):
                try:
                    (x_start, y_start, x_end, y_end) = square
                    (mask, no_mask) = predictions

                    # Дефинирање на бојата на квадратот и лабелата врз основа на тоа дали лицето има маска или не
                    if mask > no_mask:
                        label = "Nosi maska"
                        color = (90, 222, 6)
                        cnt_mask += 1
                    else:
                        label = "Ne nosi maska"
                        color = (55, 6, 222)
                        cnt_no_mask += 1

                    # Додавање на лабелата и квадратот околу лицето во излезниот стрим
                    cv2.rectangle(img, (x_start - 2, y_start - 25), (x_start + 120, y_start), color, -1)
                    cv2.putText(img, label, (x_start, y_start - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color=(255, 255, 255), thickness=1)
                    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), color, 2)
                    flag = True

                except Exception as e:
                    pass

        # Доколку е детектирано барем едно лице на фрејмот со/без маска
        if flag:
            # Испраќање на информација за тоа во дадениот момент колку лица се детектирани со/без маска
            mask_detection_msg = "[" + str(current_time) +"]: BROJ NA LICA SO MASKA: " + str(cnt_mask) +". BROJ NA LICA BEZ MASKA: " + str(cnt_no_mask)
        pub.publish(String(mask_detection_msg))
        cv2.imshow('CAMERA02', img)
        cv2.waitKey(5)

    # Инкрементирање на бројачот на фрејмови
    cnt +=1

    


def video_processing_node():
    # Иницијализација на јазолот
    rospy.init_node('video_processing_node')
    rospy.Subscriber('frame', Image, callback)
    rospy.spin()


if __name__ == "__main__":
    video_processing_node()

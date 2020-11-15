# import cv2
# from random import *
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # img = cv2.imread(
# #     "taarak.jpg")
# webcam = cv2.VideoCapture(0)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face_cordinate = face_cascade.detectMultiScale(gray)
# print(face_cordinate)


# for (x, y, w, h) in face_cordinate:
#     cv2.rectangle(img, (x, y), (x+w, y+h),
#                   (randrange(128, 326), randrange(128, 326), randrange(128, 326)), 2)

# # (x, y, w, h) = face_cordinate[5]
# # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), 2)
# # (x, y, w, h) = face_cordinate[6]
# # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), 2)
# # (x, y, w, h) = face_cordinate[7]
# # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), 2)

# cv2.imshow("Tarushjreddy", img)
# cv2.waitKey()
# print("osmairam")
import cv2
from random import *
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv2.imread(
#     "taarak.jpg")
webcam = cv2.VideoCapture(0)
while True:
    sucessfull_frame_read, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cordinate = face_cascade.detectMultiScale(frame)
    print(face_cordinate)

    for (x, y, w, h) in face_cordinate:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (0, 226, 0), 5)
    cv2.imshow("Tarushjreddy", frame)
    cv2.waitKey(1)

# webcam.release()
# print(face_cordinate)
# for (x, y, w, h) in face_cordinate:
#     cv2.rectangle(img, (x, y), (x+w, y+h),
#                   (randrange(128, 326), randrange(128, 326), randrange(128, 326)), 2)

# (x, y, w, h) = face_cordinate[5]
# cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), 2)
# (x, y, w, h) = face_cordinate[6]
# cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), 2)
# (x, y, w, h) = face_cordinate[7]
# cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), 2)


print("osmairam")

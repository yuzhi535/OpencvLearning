# *_coding=utf-8_*
# yuxi   当前系统用户
# 2021/10/20   当前系统日期
# 20:40   当前系统时间
# PyCharm   创建文件的IDE名称

import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("can't open the camera!")
    exit(-1)

window_name = 'canny'

cv.namedWindow(window_name, cv.WINDOW_NORMAL)

while 1:
    _, frame = cap.read()
    imgray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cv.imshow(window_name, frame)
    if cv.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv.destroyWindow(window_name)

import numpy as np
import argparse
import imutils
import cv2 as cv

# 构造参数解析并分析参数
arg = argparse.ArgumentParser()
arg.add_argument("--image", "-i", required=True, help="path to the image file")
args = vars(arg.parse_args())
image = cv.imread(args['image'])
grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#
ddepth = cv.CV_32F if imutils.is_cv2() else cv.CV_32F
gradX = cv.Sobel(grayImage, ddepth=ddepth, dx=1, dy=0, ksize=-1)
gradY = cv.Sobel(grayImage, ddepth=ddepth, dx=0, dy=1, ksize=-1)

gradient = cv.subtract(gradX, gradY)
gradient = cv.convertScaleAbs(gradient)

cv.namedWindow("dst", cv.WINDOW_NORMAL)
cv.namedWindow("src", cv.WINDOW_NORMAL)

blurred = cv.blur(gradient, (9, 9))

(_, thresh) = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (21, 7))
closed = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel=kernel)

closed = cv.erode(closed, None, iterations=4)
closed = cv.dilate(closed, None, iterations=4)

cv.imshow("dst", gradient)

cv.imshow("src", image)

cv.waitKey(0)

import cv2 as cv
import numpy as np


def Hough(img):
    pass


def OTSU(img):
    pass


def get_image(filepath):
    img = cv.imread(filepath)
    return img


def show_image(img):
    cv.imshow("namedWindow", img)
    key = cv.waitKey(0)


if __name__ == "__main__":
    filename = "./images/circle.jpg"
    show_image(get_image(filename))


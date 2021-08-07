import cv2 as cv
import numpy as np

img = cv.imread('/home/sasuke/Pictures/汇编语言1.png')

kernel = np.array([[1, 2, 1], [2, 0, 2], [1, 2, 1]], dtype=np.uint8)

dst = cv.filter2D(img, 3, kernel=kernel)
dst = cv.filter2D(dst, 3, kernel=kernel)

cv.imshow('src', img)
cv.imshow('dst', dst)
cv.waitKey(0)

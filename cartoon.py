import cv2 as cv
from matplotlib.pyplot import contour
import numpy as np


# Colour Quantization
def ColourQuantization(image, K=9):
    Z = image.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    _, label, center = cv.kmeans(
        Z, K, None, criteria, 1, cv.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((image.shape))
    return res2


# to get countours
def Countours(image):
    contoured_image = image
    gray = cv.cvtColor(contoured_image, cv.COLOR_BGR2GRAY)
    edged = cv.Canny(gray, 200, 200)
    contours, hierarchy = cv.findContours(
        edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[-2:]
    cv.drawContours(contoured_image, contours,
                    contourIdx=-1, color=6, thickness=1)
    return contoured_image


def main():
    cap = cv.VideoCapture(0)
    cv.namedWindow('cartoon')

    if not cap.isOpened():
        print('cannot open the camera')
        exit(-1)

    while True:
        ret, frame = cap.read()
        # frame = cv.resize(frame, (800, 600))
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        out = Countours(frame)
        out = ColourQuantization(out)
        cv.imshow('cartoon', out)

        if (cv.waitKey(30) == ord('q')):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()

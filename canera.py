import cv2 as cv

cap = cv.VideoCapture(0)
cv.namedWindow("dst", cv.WINDOW_NORMAL)

while 1:
    _, frame = cap.read()
    cv.imshow("dst", frame)
    if cv.waitKey(10) == 27:
        break

cap.release()
cv.destroyAllWindows()

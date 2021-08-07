import cv2 as cv
import numpy as np

img = cv.imread(r'/home/sasuke/Pictures/opensuse.png', 1)

h, w = img.shape[:2]
dst_size = (int(w * 1.5), int(h * 1.5))
result = cv.resize(img, dst_size)

# dst_size = (int(w * 1.5), int(h * 1.5))
# dst = cv.resize(img, dst_size, interpolation=cv.INTER_LINEAR)

# cv.imshow('img', img)
dst = img

# cv.imshow('nearest', dst)

im = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)

ret, im = cv.threshold(im, 160, 255, cv.THRESH_BINARY)

# im = cv.cvtColor(im, cv.COLOR_GRAY2BGR)

src = im.astype(np.uint8)
cnts, hie = cv.findContours(src, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
mask = np.zeros(src.shape, np.uint8)
im_fill = cv.drawContours(mask, cnts, -1, (255, 0, 0), -1)
re = np.subtract(im_fill, src)

contours, hies = cv.findContours(im_fill, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
for i in range(len(contours)):
    (x, y), radius = cv.minEnclosingCircle(contours[i])
    center, radius = (int(x), int(y)), int(radius)
    print(center)
    cv.circle(dst, center, radius, (234, 23, 234), 2)

cv.imshow('dst', im)
cv.imshow('im', dst)

if cv.waitKey(0) == 27:
    cv.destroyAllWindows()

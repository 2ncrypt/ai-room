import sys
import numpy as np
import cv2

src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch04/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# dst = cv2.bilateralFilter(src, -1, 10, 5)
# dst1 = cv2.bilateralFilter(src, -1, 100, 5)

for d in(10,50,100):
    dst = cv2.bilateralFilter(src, -1, d, 5)
    cv2.imshow('dst', dst)
    cv2.waitKey()
# cv2.imshow('src', src)
# cv2.moveWindow('src', 31, 300)
# cv2.imshow('dst', dst)
# cv2.moveWindow('dst', 530, 300)
# cv2.imshow('dst1', dst1)
# cv2.moveWindow('dst1', 1000, 300)
# cv2.waitKey()

cv2.destroyAllWindows()

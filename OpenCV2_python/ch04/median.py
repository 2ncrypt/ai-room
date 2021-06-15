import sys
import numpy as np
import cv2

src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch04/noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.moveWindow('src', 51, 50)
cv2.imshow('dst', dst)
cv2.moveWindow('dst', 560, 50)
cv2.waitKey()

cv2.destroyAllWindows()

import sys
import numpy as np
import cv2


src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch03/candies.png')
#src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# (B,R,G)
dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.moveWindow('src', 20, 50)

#RGB 밝은 영상이 들어왔을떄는 좋고
cv2.imshow('dst1', dst1)
cv2.moveWindow('dst1', 700, 30)

#HSV 흑백영상을 받았을때는 밝기정보를 함께받는 HSV가 좋음.
cv2.imshow('dst2', dst2)
cv2.moveWindow('dst2', 700, 500)

cv2.waitKey()

cv2.destroyAllWindows()

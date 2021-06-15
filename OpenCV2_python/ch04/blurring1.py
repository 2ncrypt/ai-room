import sys
import numpy as np
import cv2


src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch04/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 3x3일때 사용 할수 있는 2가지 방법

##1번째 일일이 평균값으로 곱해 blur filtering 효과
#kernel = np.ones((3, 3), dtype=np.float64) / 9.
#dst = cv2.filter2D(src, -1, kernel)

##2번째 cv2의 blur함수 사용
dst = cv2.blur(src, (3, 3))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

import sys
import numpy as np
import cv2


src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0
#numpy.clip(arrat,min,max) : array내의 element들에 대해서 min 값보다 작은 값들은 min값으로 바꾸고, max값봐 큰 값들을 max값으로 바꿔주는 함수.
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.moveWindow('src', 20, 50) 
#이미지가 뜨는 위치를 지정 여러개 겹쳐서 나올때 편함.
cv2.imshow('dst', dst)
cv2.moveWindow('dst', 700, 50)
cv2.waitKey()

cv2.destroyAllWindows()

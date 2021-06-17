import sys
import numpy as np
import cv2


src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.moveWindow('src', 31, 300)
cv2.imshow('dst', dst)
cv2.moveWindow('dst', 800, 300)
cv2.waitKey()
cv2.destroyAllWindows()

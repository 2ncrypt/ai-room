import sys
import numpy as np
import cv2


src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]
print(h,w)
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))

cv2.imshow('src', src)
cv2.moveWindow('src', 31, 300)
cv2.imshow('dst', dst)
cv2.moveWindow('dst', 800, 300)
cv2.waitKey()
cv2.destroyAllWindows()

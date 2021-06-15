import sys
import numpy as np
import cv2

src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch04/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2)
dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.moveWindow('src', 50, 50)
cv2.imshow('dst', dst)
cv2.moveWindow('dst', 100, 500)
cv2.waitKey()

cv2.destroyAllWindows()

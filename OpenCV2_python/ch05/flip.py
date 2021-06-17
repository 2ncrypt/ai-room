import sys
import numpy as np
import cv2


src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

for f in (-1,0,1):
    dst = cv2.flip(src, f , dst=None)
    cv2.imshow(f'{f}',dst)
    cv2.moveWindow(f'{f}', 30, 300)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()

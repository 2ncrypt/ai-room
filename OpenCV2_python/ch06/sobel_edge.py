import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch06/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)

# # #창하나에 보기
# fig, ax = plt.subplots(2, 2, figsize=(10, 10), sharey=True)
# fig.canvas.set_window_title('test')
# ax[0][0].imshow(src)
# ax[0][1].imshow(mag)
# ax[1][0].imshow(dst)
# plt.show()

cv2.imshow('src', src)
cv2.moveWindow('src', 31, 300)
cv2.imshow('mag', mag)
cv2.moveWindow('mag', 500, 300)
cv2.imshow('dst', dst)
cv2.moveWindow('dst', 1000, 300)
cv2.waitKey()

cv2.destroyAllWindows()

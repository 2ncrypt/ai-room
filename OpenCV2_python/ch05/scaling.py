import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch05/rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

##cv2 imshow
# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1[500:900, 400:800])
# cv2.imshow('dst2', dst2[500:900, 400:800])
# cv2.imshow('dst3', dst3[500:900, 400:800])
# cv2.imshow('dst4', dst4[500:900, 400:800])

# ##plt
fig, ax = plt.subplots(2, 2, figsize=(10, 10), sharey=True)
fig.canvas.set_window_title('dst1~4')
# # 그림마다 픽셀의 눈금 없애기
# ax[0][0].axis('off')
# ax[0][1].axis('off')
# ax[1][0].axis('off')
# ax[1][1].axis('off')
# # 그림 비율 유지
# ax[0][0].imshow(dst1, aspect="auto")
# ax[0][1].imshow(dst2, aspect="auto")
# ax[1][0].imshow(dst3, aspect="auto")
# ax[1][1].imshow(dst4, aspect="auto")
# plt.show()

#2차
plt.subplot(221), plt.axis('off'), plt.imshow(dst1[500:900, 400:800], 'gray'), plt.title('dst1')
plt.subplot(222), plt.axis('off'), plt.imshow(dst2[500:900, 400:800], 'gray'), plt.title('dst2')
plt.subplot(223), plt.axis('off'), plt.imshow(dst3[500:900, 400:800], 'gray'), plt.title('dst3')
plt.subplot(224), plt.axis('off'), plt.imshow(dst4[500:900, 400:800], 'gray'), plt.title('dst4')
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()

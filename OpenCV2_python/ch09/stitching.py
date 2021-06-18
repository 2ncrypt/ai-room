import sys
import numpy as np
import cv2


img_names = ['/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch09/img1.jpg', '/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch09/img2.jpg', '/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch09/img3.jpg']

imgs = []
for name in img_names:
    img = cv2.imread(name)

    if img is None:
        print('Image load failed!')
        sys.exit()

    imgs.append(img)

# print(cv2.__version__)
stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print('Stitch failed!')
    sys.exit()

cv2.imwrite('output.jpg', dst)

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', dst)
cv2.moveWindow('dst', 100, 300)

dst_blur= cv2.GaussianBlur(dst, (0,0), 3) #3 = sigma
cv2.imshow('dst', dst)
cv2.moveWindow('dst', 500, 300)

cv2.waitKey()
cv2.destroyAllWindows()

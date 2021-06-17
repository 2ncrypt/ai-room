import sys
import numpy as np
import cv2


# 영상 불러오기
src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch09/graf1.png')
src1 = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch09/graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch09/graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
# feature = cv2.KAZE_create()
feature = cv2.AKAZE_create()
# feature = cv2.ORB_create()

# 특징점 검출
kp1 = feature.detect(src1)
kp2 = feature.detect(src2)

print(f'{feature} of kp1:', len(kp1))
print(f'{feature} of kp2:', len(kp2))

# 검출된 특징점 출력 영상 생성
dst1 = cv2.drawKeypoints(src1, kp1, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('src', src)
cv2.moveWindow('src', 500, 10)
cv2.imshow('dst1', dst1)
cv2.moveWindow('dst1', 100, 300)
cv2.imshow('dst2', dst2)
cv2.moveWindow('dst2', 900, 300)
cv2.waitKey()
cv2.destroyAllWindows()

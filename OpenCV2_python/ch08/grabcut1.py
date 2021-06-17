import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch08/nemo.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할
rc = cv2.selectROI(src)
mask = np.zeros(src.shape[:2], np.uint8)

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[:, :, np.newaxis] 
#newaxis 들어가는 배열이 3x3으로 들어갈때 return 골격을 자기가 만들어줌
#newaxis는 차월을 변경해줌

mask =mask *64

# 초기 분할 결과 출력
cv2.imshow('mask', mask)
cv2.moveWindow('ROI selector', 800, 300)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()

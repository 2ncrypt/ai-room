import sys
import numpy as np
import cv2


src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch07/keyboard.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

#threshold python에서 return값을 사용하지 않을때
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

##그레이컬러에서 컬러로 바운것은
#바운딩박스에 컬러를 넣기를 위해선 컬러가 필요하니까
#그레이컬러의 좌표 정보는 src_bin ,_에서 이미 다 뽑았기때문에
#바운딩박스의 컬러만이 필요
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]

    if area < 20:
        continue

    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))

cv2.imshow('src', src)
cv2.moveWindow('src', 31, 300)

cv2.imshow('src_bin', src_bin)
cv2.moveWindow('src_bin', 500, 300)

cv2.imshow('dst', dst)
cv2.moveWindow('dst', 900, 300)
cv2.waitKey()
cv2.destroyAllWindows()

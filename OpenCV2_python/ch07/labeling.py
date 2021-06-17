import sys
import numpy as np
import cv2


mat = np.array([
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)

#connectedComponents는 레이블링 함수
cnt, labels = cv2.connectedComponents(mat) 
## =>retval : 객체개수 N을 반환하면 [0,N-1]의 레이블 존재 0은 배경
## =>labels : 영상과 같은 크기이고 numpy.ndarray gudtlr

print('sep:', mat, sep='\n')
print('cnt:', cnt)
print('labels:', labels, sep='\n')
print('=====================================')
retval, labels, stats, centroids = cv2.connectedComponentsWithStats(mat)

print('retval:', retval, sep='\n')
print('labels:', labels, sep='\n')
print('stats:', stats, sep='\n')
print('centrodis:', centroids, sep='\n')
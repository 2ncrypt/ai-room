import sys
import numpy as np
import cv2


src = cv2.imread('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch06/dial.jpg', cv2.COLOR_BGR2GRAY)
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
dst = cv2.GaussianBlur(src, (0,0), 1)


# def on_trackbar(pos):
#     rmin = cv2.getTrackbarPos('minRadius', 'img') 
#     rmax = cv2.getTrackbarPos('maxRadius', 'img')
#     th = cv2.getTrackbarPos('threshold', 'img')

#     circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
#                                param1=120, param2=th, minRadius=rmin, maxRadius=rmax)
#     dst = src.copy()
#     if circles is not None:
#         for i in range(circles.shape[1]):
#             cx, cy, radius = circles[0][i]
#             cv2.circle(dst, (cx, cy), int(radius), (0, 0, 255), 2, cv2.LINE_AA)
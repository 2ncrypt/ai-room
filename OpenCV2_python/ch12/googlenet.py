import sys
import numpy as np
import cv2

# 입력 영상 불러오기

filename = '/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch12/Pera.jpg'

if len(sys.argv) > 1:
    filename = sys.argv[1]

img = cv2.imread(filename)

if img is None:
    print('Image load failed!')
    sys.exit()

# 네트워크 불러오기

# Caffe
model = '/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch12/googlenet/bvlc_googlenet.caffemodel'
config = '/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch12/googlenet/deploy.prototxt'

net = cv2.dnn.readNet(model, config)

if net.empty():
    print('Network load failed!')
    sys.exit()

# 클래스 이름 불러오기

classNames = None
with open('/Users/hyunsul/Desktop/ai-room/OpenCV2_python/ch12/googlenet/classification_classes_ILSVRC2012.txt', 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# 추론

blob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 117, 123))
net.setInput(blob)
prob = net.forward()

# 추론 결과 확인 & 화면 출력

out = prob.flatten()
classId = np.argmax(out)
confidence = out[classId]

text = f'{classNames[classId]} ({confidence * 100:4.2f}%)'
cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.moveWindow('img', 300, 300)
cv2.waitKey()
cv2.destroyAllWindows()

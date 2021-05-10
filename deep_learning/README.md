# **딥러닝**

인공지능 > 머신러닝 > 딥러닝

데이터 : 딥러닝은 데이터를 이요해 예측 또는 판별을 수행
지도학습(분류, 회귀) vs 비지도학습(GAN, Auto Encoder)

텐서플로우 기초 : https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/

모두의 딥러닝  : https://github.com/gilbutITbook/080228



## 1장

첫번째 딥러닝 코드 : first_deep_learning.ipynb
커널이 죽는 오류 해결 후 코드를 실행하니 정상적으로 출력이됨
이 코드를 기반으로 어떠한 원리로 딥러닝이 실행되는지 확인 해야함.

from tensorflow.keras.models import Sequential 
이때 Sequential 을 실행시키면 한 줄의 신경망이 만들어짐.

각각 쓰이는 용어들이 많으니 설명을 들을때마다 왠만하면 주석처리로 소스에 붙여놓기

## 2장

딥러닝을 자세하게 들어가려면 기초 수학이 되어야함. 미분이 자주 나오니까 한번은 공부하는걸로
편미분도 자주 나온뎅 개싫당

딥러닝에 관한 기초 수학분야.
후에 모듈이나 함수를 쓸때 해당 관련 내용이 많이 나오니 따로 공부해야할 필요성이 있음.

## 3장(예측성 긋기 : 선형회귀)

독립 변수 : 독립적으로 변할 수 있는 x값
종속 변호 : 독립 변수에 따라 종속적으로 변하는 값
선형 회귀 : 독립 변수 x를 사용해 종속 변수 y의 움직임을 예측하고 설명하는 작업
단순 선형 회귀(simple linear regression) : 하나의 x값 만으로도 y값 설명 가능
다중 선형 회귀(multiple linear regression) : y값 설명에 x값이 여러 개 필요할 때

![image-20210510121822501](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210510121822501.png) **예시**












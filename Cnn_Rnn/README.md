# 2021.5.17

## PDF(1~59) 

Convolutional Neural Networks(CNN)의 목적 : 
![image-20210517185023604](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517185023604.png)
Input Layer를 I , Hidden Layer를 W라고 할 때 효과적으로 W를 학습시키기 위하여. 

<img src="/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517185218581.png" alt="image-20210517185218581 image-50px" style="zoom:50%;" />
Feature Map = (w * h) * c = Metrics연산
Image를 계산한것? 이라고 생각하면 되나
Feature Map의 갯수는 C의 갯수와 같다.

CNN의 순서는
Input Image => Concolution(Learned) => Non-linearity = > Spatial pooling => Feature Maps => End
순으로 이루어짐
Pooling에는 여러가지 방법이 있어서 뒤에서 따로 다룸.

![image-20210517190254254](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517190254254.png)
Convolution Layer는 filter에 걸러진 것만 사용.
보통 결과는 Activate Function 중 Softmax를 사용한 결과.(확률의 특징은 값을 다 더하면 1)

Fully Connected Layer(FC layer)
연산 방식은 Metrics연산 법과 동일함
일반적인 컬러연산은 R G B 3개의 채널(3D)로 이루어져서 연산을 하려면 1D로 변환하여야함.
(w * h) * c 
![image-20210517190906555](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517190906555.png)
1D Vector라고도 칭함
위의 그림에서 A와 B가 곱해지려면 A의 Column과 B의 Row가 같아야함.
그리고 일반적으로 (x,y)라고 표기하던 것과 달리 (Row, Column)으로 표기함.

Convolution Layer
그림이 많아 사진으로 대체
![image-20210517191228814](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517191228814.png)
![image-20210517191251287](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517191251287.png)
![image-20210517191319849](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517191319849.png)

Convolution Layer : Dilated Convolution 
이 연산으로 얻을 수 있는것
장점 : 계산량은 3 * 3과 동일
단점 : 정보를 놓치는 경우가 발생 할 수 있다.
이러한 연산이 가능한 이유
영상에는 특별한 특징이 있는데 256,256,256 이렇게 숫자는 크고 경우의 수는 많지만 자연계의 색이라고 할 수 있는 수는 많지 않음
그래서 인접한 픽셀의 밝기는 비슷해서 Dilated연산을 해도 굳이 상관이 없음.
![image-20210517191718554](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517191718554.png)

Dilated연산의 적용
![image-20210517191748113](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517191748113.png)

Convolution Layer : Transposed Convolution
연산법
![image-20210517192505020](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517192505020.png)

결과 
![image-20210517193206433](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517193206433.png)

Stride를 하게되면
![image-20210517193428349](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517193428349.png)

Pooling과 Stride의 차이
Pooling은 주어진 데이터에서만 연산

여기서도 연산할때 w, h를 잘 맞춰야함 아니면 Error뜸
![image-20210517193705807](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517193705807.png)

Convolution with padding
패딩을 그냥 하게되면 데이터가 없어서 안되는 경우가 허다함.
그래서 패딩에는 4가지 방법이있음.
![image-20210517200449560](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517200449560.png)
ㄴㅏ머지 한 가지는 ZeroPadding인데 위의 3가지와는 다르게 빈 공간에 전부 0으로 채우는것
Pytorch에서는 padding_mod='mode'로 사용

Convolution Layer : 1 * 1 convolution
굳이 1*1 convolution을 하는 이유는 
FeatureMap의 C축을 의도적으로 늘리고 싶을때나, 줄이고싶을때
![image-20210517200645849](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517200645849.png)

Pooling Layers
하는 이유는 representation을 더 작게 만들기 위하여
![image-20210517200735988](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517200735988.png)

Max Pooling은
![image-20210517200752168](/Users/hyunsul/Library/Application Support/typora-user-images/image-20210517200752168.png)
 값이 이러하고, 2x2 filter일때 제일 큰값만 가져와 featuremap을 만드는것. 

## 소스코드(내일할랭)


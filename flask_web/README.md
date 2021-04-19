Flask 관련 필기

__&&__ 같은건 내장 변소
ex) __name__ 등등


.debug = True #오류를 웹페이지 상에 띄워주기때문에 사용. 하지만 실제 오픈 시에는 서버의 자료목록이 다 보이므로 사용하지 않거나 False

@.route('파일위치', methods=['Get or POST']) : 웹을 파일위치부터 받아 온다는것

def index():
    # return "Welcom to hell"
    return render_template("index.html",data="Kim") 
    #렌더 템플릿을 이용하여 index.hmtl을 보여줌
    #랜더 템플릿은 첫번째 인자로 html파일 경로, 두번째로 인자로 전달할 데이터를 받음
    #렌더 템플릿은 {{$$$}}안에 파이썬 코드(여기선 변수)가 있으면 그 파이썬 코드를 html로 바꿔줌.

################ 사용 예제 ################
    #렌더 템플릿은 jinja2 기반
    #{{...}} : 변수나 표현식의 결과를 출력하는 구분자
    #{%...%} : if문이나 각종 제어문

예제 주소
templates/includes/layouts.html

{% block body %} 
    <!-- 이렇게 해놓으면 body태그를 블록으로 잡아 다른 곳에서는 위아래에 있는 기본 설정값을 입력하지 않아도 된다. -->
{% endblock %}

사용법
python 에서 import  받는것처럼 이건 jinja2의 문법이기 떄문에 
{% extends "includes/layouts.html"%} 
<!-- 진자 엔진의 import방법 = extends -->
{% block body %}
{{data}}
<h1>welcome to hell!!</h1>
{% endblock %}

위와 같이 사용

from flask import Flask , render_template
from data import Articles

app = Flask(__name__) #__&&__ 는 내장변수

app.debug = True #오류를 웹폐이지 상에 띄워줌(단점 나의 폴더 목록도 다 보이기 떄문에 개발 할 때만 True)

@app.route('/main', methods=['GET']) #route : 중계하다 , @ : decorate // /data 폴더의 뒤로 경로 지정
def index():
    # return "Welcom to hell"
    return render_template("main.html") 
    #렌더 템플릿을 이용하여 index.hmtl을 보여줌
    #랜더 템플릿은 첫번째 인자로 html파일 경로, 두번째로 인자로 전달할 데이터를 받음
    #렌더 템플릿은 {{$$$}}안에 파이썬 코드(여기선 변수)가 있으면 그 파이썬 코드를 html로 바꿔줌.
    ################ 사용 예제 ################
    #렌더 템플릿은 jinja2 기반
    #{{...}} : 변수나 표현식의 결과를 출력하는 구분자
    #{%...%} : if문이나 각종 제어문

@app.route('/abt')
def about():
    return render_template("about.html", hello = "Hyunsul Kim")

@app.route('/art')
def articles():
    articles = Articles()
    # for _ in range(0,2):
    #     print(articles[_]['body'])
    return render_template("articles.html",article = articles)

@app.route('/article/<int:id>') #<>는 params
def article(id):
    articles = Articles()
    article = articles[id-1]
    return render_template("article.html", article = article)

if __name__ == '__main__': #모듈의 시작점을 만듦, 프로그램의 시작점일 떄만 아래의 코드 실행
    app.run()
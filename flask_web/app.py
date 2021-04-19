from flask import Flask

app = Flask(__name__) #__&&__ 는 내장변수

app.debug = True #오류를 웹폐이지 상에 띄워줌(단점 나의 폴더 목록도 다 보이기 떄문에 개발 할 때만 True)


if __name__ == '__main__': #모듈의 시작점을 만듦, 프로그램의 시작점일 떄만 아래의 코드 실행
    app.run()
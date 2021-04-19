#그냥 함수 모음집 만들기 Project

def print_line():
   print('=====================================================')

def print_circle(radius):
    r = 3.14
    print('원의 반지름 : ', radius)
    print('원의 면적 : ', r * radius * radius) 
    print('원의 둘레 : ', 2.0 * r * radius)

def _2cha(a,b,c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print(f'해는 {r1} 또는 {r2}')

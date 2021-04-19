#continue, break
import Ddef as D

D.print_line()
st = input("Input word : ")
print(f'총 글자 갯수 : {len(st)}')
mm = ['a', 'e', 'i', 'o', 'u']
count = 0

for ch in st:
    if ch in mm:
        count = count + 1
        continue
    print(ch)
print(f'끝!! 빠진 알파벳 갯수 : {count}')

D.print_line()
# D.print_circle(3)  #잘되네
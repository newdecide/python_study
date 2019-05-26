# (1) key값이 최소 3개 이상인 dictionary를 최소 3개 포함한 리스트를 csv파일로 만들어서 저장하는 함수를 만드세요
# (2) 저장한 csv 파일을 불러와서 다시 dictionary로 변환하는 함수를 만드세요.

# with

f= open("./test.txt", 'w')
# f.blah

f.close

with open('./new.txt', 'w') as f: #f = open()
    f.write("안녕하세요! with입니다.")
    # 들어쓰기끝나면 자동으로 파일을 닫아준다.
if not f.closed:
    print("파일이 꺼지지 않았습니다... 큰일났어요..")

print(dir(f))
# '__exit__' 있기때문에 자동으로 종료된다.
# dir() 기능들을 확인할 수 있다.
# strip 지우기 대문자화 upper 

# 모듈(module) 프로그램(기능)의 모음

def add_all(*args):
    return sum(args)


import _0526
print(_0526.add_all(1,2,3,4,5))
from _0526 import add_all
print(add_all(1,2,3,4))
# 1-10 함수

# 추상화 별도의 공간에 존재하여 변수간 간섭되는 방해를 일으키지 않는 방법

# 분리 코드는 다른곳에 작성되어, 우리가 필요한 경우 호출만 하여 사용할 수 있는 방법

# 함수 만드는 법
# def func_name(arg):
#     #코드 작성
#     print("hello, func")
#     return arg # 리턴 없을시 생략가능

def print_hello_world():
    print("Hello World!")

# hello world text 함수
print_hello_world()

# a+4 함수
def add_4(a):
    return a+4

result = add_4(5) # 4 + 5 = 9

print("4+5=", result)

def add(a,b):
    return a+b
result = add(5,5)
print("5+5", result)

def add1(num):
    return num + 1

print("1+1=", add1(1))
print("1+3=", add1(3))
print("(1+(1+(1+3)))=", add1(add1(add1(3))))


def add_mark(string):
    return string +'!'

print(add_mark('Python'))

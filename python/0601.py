from functools import reduce

a = list(range(10+1))

result = reduce(lambda x, y: x+y, a)
print(result)

a = [1,2,3]

result = reduce(lambda x, y: x**2+y**2, a)
print("x**2 + y**2=",result)

# 1~10 까지 가진 리스트에서 각 요소의 제곱을 더하세요.

def make_print_start_end(func):
    # def new_func(a, b, c):
    def new_func(*args, **kwargs): # 패킹
        print("함수가 시작됩니다.")
        # result = func(a, b, c)
        result = func(*args, **kwargs) # 언패킹
        print("함수가 끝났습니다.")
        return result
    return new_func

@make_print_start_end # 기능이 자동으로 이어진다.
def print_a_to_b(a, b, c):
    for i in range(a, b+1, c):
        if i < b:
            print(i, end =', ')
        else:
            print(i)
# new_func = make_print_start_end(print_a_to_b)
# new_func(1, 100, 3)

@make_print_start_end
def sum_a_to_b(a,b):
    result = 0
    for i in range(a, b+1):
        result += i
    return result

# new_func2 = make_print_start_end(sum_a_to_b)
# print(new_func2(1,10))

result = sum_a_to_b(1, 100)
print(result)

# decorator
from time import time

def check_time(func):
    def new_func(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print('함수가 걸린 시간은 : ', end_time - start_time)
        return result
    return new_func

@check_time
def sum_1_to_n(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

result = sum_1_to_n(1234000)
print(result)

@check_time
def gauss_sum(n):
    return(n * (n+1))/2

result = gauss_sum(12340000)
print(result)
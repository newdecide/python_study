# 병합정렬 O(n log n)
from random import choice

raw_list = list(range(0, 100+1)) # 0~100까지 리스트

# 랜덤으로 정렬 리스트 만들기
target = []
for _ in range(100): # 0~99까지 랜덤 리스트
    target.append(choice(raw_list))

# A리스트와 B리스트를 합치는 함수 정의
def _merge(A, B):
    result = [] # 결과담을 리스트
    length = len(A) + len(B) # A와 B 합친 길이

    for _ in range(length):
        try:
            if A[0] > B[0]:
                result.append(B[0])
                B.remove(B[0])
            else:
                result.append(A[0])
                A.remove(A[0])
        except IndexError:
            if len(A):
                result += A
                break
            else:
                result += B
                break
    return result

# 왼쪽 오른쪽으로 값을 나눈다.
def merge_sort(A):
    if len(A) < 2: # 재귀사용 길이가 2보다 작다면 정렬할게 1개밖에 안남기에 바로 A 리턴
        return A
    left_list = merge_sort(A[:len(A) // 2]) # 왼쪽 A 전체 리스트
    right_list = merge_sort(A[len(A) // 2:]) # 오른쪽 A 전체 리스트

    return _merge(left_list, right_list) # 합치는 함수 호출

    

print("병합정렬 수행 : ",merge_sort(target))

# 메모라션제이션 fibonaci
from time import time

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

MEMO = {}

def fib2(n):
    if n <= 2:
        return 1
    if MEMO.get(str(n-1)):
        fib_n_1 = MEMO[str(n-1)]
    else:
        fib_n_1 = fib(n-1)
        MEMO[str(n-1)] = fib_n_1
    if MEMO.get(str(n-2)):
        fib_n_2 = MEMO[str(n-2)]
    else:
        fib_n_2 = fib(n-2)
        MEMO[str(n-2)] = fib_n_2
    f_n = fib_n_1 + fib_n_2
    return f_n

# 시간체크 함수
def check_time(func):
    def new_func(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print('함수가 걸린 시간은 : ', end_time - start_time)
        return result
    return new_func
    
@check_time
def find_fib(n):
    return fib(n)

print("피보나치 결과: ",find_fib(12))

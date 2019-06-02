# 알고리즘 계산복잡도
# Big O 표기법 O(n), O(1) Big-O Complexity
# 선택, 삽입, 병합, 퀵 (선택, 병합)

# 선택정렬 O(n^2)
# 랜덤한 숫자를 포함하는 리스트를 역순으로 선택정렬하는 함수를 만드세요
from random import choice

raw_list = list(range(0, 100+1)) # 0~100까지 리스트

# 랜덤으로 정렬 리스트 만들기
target = []
for _ in range(100): # 0~99까지 랜덤 리스트
    target.append(choice(raw_list))

# 정렬전 
print("선택정렬 실행 전")
print(target)
# 오름차순
def selection_sort(A):
    result = []
    
    while len(A) != 0:
        min_num = 100
        for i in A:
            if min_num > i:
                min_num = i
        result.append(min_num)
        A.remove(min_num)
    return result

print("선택정렬 오름차순 실행 후: ", selection_sort(target))



target = []
for _ in range(100):
    target.append(choice(raw_list))

# 정렬전 
print("선택정렬 실행 전")
print(target)

# 내림차순
def selection_sort_dec(A):
    result = []

    while len(A) != 0:
        max_num = 0
        for i in A:
            if max_num < i:
                max_num = i
        result.append(max_num)
        A.remove(max_num)
    return result

print("선택정렬 내림차순 실행 후 ",selection_sort_dec(target))



raw = [0,1]
target = []
for _ in range(100):
    target.append(choice(raw))

def solution(A):
    length = len(A)
    sum_1 = sum(A)
    string_value = '0' * (length - sum(A)) + '1' * sum_1
    return list(map(int, list(string_value)))

print("0,1을 랜덤으로 뿌린 리스트 정렬전")
print(target)
print("오름 차순 정렬: ",solution(target))



# -50~50 일 경우 최소값음 -50 리스트의 0번째 요소를 기준으로 하면된다. A[0]
raw = list(range(-50, 50+1)) # -50부터 ~ 50까지

target = []
for _ in range(100):
    target.append(choice(raw))

print("-50부터 ~ 50까지 랜덤숫자 정렬 전", target)

def _merge(A, B):
    result = []
    length = len(A) + len(B)
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

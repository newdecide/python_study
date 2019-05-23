# del, pop, append, reverse, sort()
var = [1,2,3,5,5,6,7]
print(var)
var[3] = 4 
print("var[3] = 4 변경: ", var)
# [1, 2, 3, 4, 5, 6, 7] 
var.append(8) 
print("append(8): ", var) # [1, 2, 3, 4, 5, 6, 7, 8]

# 리스트 삭제
del var[0] 
print("del var[0] 제거: ", var) # [2, 3, 4, 5, 6, 7, 8] 

# 리스트 거꾸로 뒤집기
var.reverse() 
print(var) # [8, 7, 6, 5, 4, 3, 2] 

numbers = [1,2,3,4,5,6] 
numbers.append(7) 
numbers.append(8) 
numbers.append(9) 
numbers.append(10) 
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(numbers[0:1]) # [1]
print(numbers[0]) # 1
print(numbers[0:3]) # [1, 2, 3]
print(numbers[0:2] + numbers[-2:-1]) # [1, 2, 9] 
print(numbers[0:2] + numbers[-2:]) # [1, 2, 9, 10] 
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
numbers.reverse() 
print(numbers) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
numbers = numbers[::2] 
print(numbers) # [10, 8, 6, 4, 2]
numbers = [10, 2, 5, 4, 6, 7, 9] 
print(numbers) # [10, 2, 5, 4, 6, 7, 9]
numbers.sort() 
print(numbers) # [2, 4, 5, 6, 7, 9, 10]
print(numbers.pop(2)) # 5
print(numbers) # [2, 4, 6, 7, 9, 10] 
del numbers[0] # 첫번째 리스트 제거
print(numbers) # [4, 6, 7, 9, 10] 
del_num = numbers.pop(0) 
print(numbers) # [6, 7, 9, 10] 
del_num # 4 pop으로 나가는 변수
numbers = [1, 2, 3, 4, 6] 
print(numbers) # [1, 2, 3, 4, 6] 
numbers.insert(0,0) 
numbers # [0, 1, 2, 3, 4, 6] 
numbers.insert(-1,5) 
numbers # [0, 1, 2, 3, 4, 5, 6]
numbers2 = [7,8,9] 
numbers + numbers2 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
numbers.extend(numbers2) 
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
numbers = numbers + numbers2 
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9] 
numbers.append(1) 
numbers.append(1) 
numbers.append(1) 
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 1, 1, 1] 
print(numbers.count(1)) # 리스트에 1이 몇개인가? 4
numbers.remove(1) # 1 제거
print(numbers) # [0, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 1, 1, 1] 
numbers.remove(0) 
print(numbers) # [2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 1, 1, 1] 

# 리스트 복사: 주소를 가지고 있어 공유하면 같이 변경되게 된다, 병합
# copy 하면 값이 변경되도 같이 변경되지 않는다.

# 참거짓 타입
# 참 거짓 True, False 
# Type: Boolean
# True, False, ==, !=, in, not in 
# <, <=, >, >= 
# bool()
# Type : Boolean
# False 친구들 
# []: 빈리스트
# '': 빈 문자열
# 0: 숫자 0 
# None: NoneFalse 친구들

# 프로그램 흐름 제어
# 01-06~07 흐름제어(if, for, while)
#if
if 3 < 5:
    print("3은 5보다 작습니다.")
# if문은 여기까지 들여쓰기 된 부분까지
print("3 > 5: 5는 3보다 큽니다.")

if 'p' in 'python':
    print("p라는 글자는 python에 포함되어 있습니다.")
# 참인경우
else:
    print("p가 포함되어 있지 않습니다.")
# 거짓인 경우

num = int(input("0~9까지 숫자를 하나 입력하세요"))
# if num > 8:
#     print("입력하신 값이 8보다 큽니다.")
# else:
#     if num > 5:
#         print("입력하신 값이 8보다 같거나 작고, 5보다는 큽니다.")
#     else:
#         if num > 2:
#             print("입력하신 값이 5보다 같거나 작고, 2보다는 큽니다.")
#         else:
#             print("입력하신 값이 2보다 같거나 작습니다.")
if num > 8:
    print("입력하신 값이 8보다 큽니다.")
elif num > 5:
    print("입력하신 값이 8보다 같거나 작고, 5보다는 큽니다.")
elif num > 2:
    print("입력하신 값이 5보다 같거나 작고, 2보다는 큽니다.")
else:
    print("입력하신 값이 2보다 같거나 작습니다.")

# random, abs
# print()
# type()
# int()
# float()

import random
n=random.randint(1, 10) # 1~10까지 랜덤하게 뽑아줘
print("랜덤숫자: ", n, "이 골라졌습니다.")

print("프로그램이 종료되었습니다.")

#프로그램 흐름 제어

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
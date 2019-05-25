# 1-11 packing, unpacking, 재귀함수(예외처리)
def test(a,b,c):
    print('a는 : ', a)
    print('b는 : ', b)
    print('c는 : ', c )

test(3, b=1, c=2)

# packing 
def sum_all(*args):
    print(args)
    # return a + b + c
print(sum_all(1,2,3,4,5,6)) # (1, 2, 3, 4, 5, 6) 튜플로 만들어진다.

# def print_f_name(father, morther, sister, brother):
#     print("아버지 이름은", father)
#     print("아버지 이름은", marther)
#     print("아버지 이름은", sister)
#     print("아버지 이름은", brother)

print("")
def print_f_name(**kwargs):
    for key in kwargs:
        print(key,'의 이름은 ', kwargs[key])
print_f_name(father ="박형식",morther="문소리",sister="보니", brother = "하니", cat ="써니")
# 지우고 삭제 해도 잘 됨 편리

# unpacking
def sum_all2(*args):
    print(args)
    return sum(args)

print(sum_all2(*[1,2,3,4,5,6,7,8,9,10,11]))

family_dict = {
    "father" : "홍길동",
    "mother" : "김영희",
    "sister" : "김태희",
    "cat" : "코카"
}

def print_f_name2(**kwargs):
    for key in kwargs:
        print(key, '의 이름은', kwargs[key])
print_f_name2(**family_dict)

likes = []
def input_like():
    like = input("좋아하는걸 하나 입력하세요.")
    likes.append(like)
    print(likes)

input_like()
input_like()
input_like()

# 재귀함수

# n! => n * (n-1) * (n-2) * ... *1

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# 1~5 = 120

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(5) == 1 * 2 * 3 * 4 * 5)

# 재귀 2
def add_n(a,n):
    if n==0:
        return a
    return 1 + add_n(a, n-1) # n-1이 0이 될때까지 재귀 호출

print(add_n(110,7))
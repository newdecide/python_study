# 8회차
def square(x):
    return x ** 2

result = square(2)

print("2의 제곱은? ",result)

new_func = square
print("9의 제곱은?", new_func(9))

students = []

student1_info = {
    "first_name":"sol",
    "last_name":"hyun",
    "student_no":3498

}

student2_info = {
    "first_name":"park",
    "last_name":"won",
    "student_no":1345

}

student3_info = {
    "first_name":"zihoe",
    "last_name":"song",
    "student_no":2458
}

student4_info = {
    "first_name":"yoo",
    "last_name":"jasuk",
    "student_no":2048
}
students.append(student1_info)
students.append(student2_info)
students.append(student3_info)
students.append(student3_info)

print(students)

def sort_help(d):
    return d['student_no']

# sorted_students = sorted(students, key=sort_help)
sorted_students = sorted(students, key=lambda x: x['student_no'])
print(sorted_students)

# lambda

# a = lambda x : x+1
# a(3)
# a(5)
# a(10)

# +1 해주는 함수
a = (lambda x : x+1)(5)
print("a = lambda x :", a)
# 3개의 값을 더해주는 함수
a = (lambda x, y, z : x+y+z)(5,6,7)
print("a = lambda x+y+z :", a)
# 2개의 값을 각각 제곱해서 더해주는 함수
a = (lambda a,b : a**2 + b**2)(5,7)
print("a = lambda {}제곱+{}제곱".format(5,7), a)

# 1개의 숫자를 받아서 2의 배수이면 True, 아니면 False 리턴하는 함수
# 0~n개의 정수를 받아서 다 합쳐주는 함수

# boolean
bool1 = (lambda x : True if x % 2 == 0 else False) (10) # True
bool2 = (lambda x : True if x % 2 == 0 else False) (9) # False

print("bool1은:",bool1, ", bool2는:",bool2)

# sum
sum = (lambda *x : sum(x))(1,2,3,4,5,6,7,8,9,10) # 55
print("1~10의 합계는: ",sum)

a = list(range(1, 10+1))
print("1~10까지의 리스트",a)

result = []
for el in a:
    result.append(el+1)
print("list에 1씩 추가한 리스트",result)

map(lambda x : x+1, a)
result = map(lambda x: x+1, a)
list(result)

for e in result:
    print(e)

result = map(lambda x: x+1, a)

for el in result:
    print(el)

raw_list = list(range(1, 100+1))

result = map(lambda x: 'fizzbuzz' if x % 15 == 0 else
('fizz' if x % 3 == 0 else ('buzz' if x % 5 == 0 else x)), raw_list)

print("1~100까지 fizzbuzz: ",list(result))

# filter(func, list)

a = list(range(1, 10+1))
result = []
for el in a:
    if el % 2 == 0:
        result.append(el)
print("1~10: ",a)
print("1~10 2의 배수: ",result)

# a = filter(True, a)

# b = list(filter(True, a))

c = list(filter(lambda x : True, a)) # true 다 존재

d = list(filter(lambda x: x % 2 == 0, a)) # 2로나눠지는 것만 출력 2의 배수마내

# print(a)
# print(b)
print(c)
print(d)

# lambda 함수 이용 filter
# 1~100까지 가진 리스트에서 50보다 큰 값만 남겨보세요.

num_result = list(range(1, 101)) # 1~100까지
num50= list(filter(lambda x: x > 50, num_result))
# 위 결과값에서 2의배수만 가진 리스트 만드세요.
num50to2= list(filter(lambda x: x % 2 == 0 , num50))

print("num50은 : ", num50)
print("num50to2는 : ", num50to2)
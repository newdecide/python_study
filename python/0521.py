list(range(100))

list(range(1, 100-1))

# for i in range(100):
#     print(i)
#     if i>30:
#         break

# n = 0
# while n <= 100:
#     print(n)
#     n+=1

numbers = list(range(1, 10+1))
print("1~10까지의 합:",sum(numbers))
print("1~50까지의 합:",sum(range(1, 50+1)))

n = 0
for i in range(1, 100+1):
    if i%2 == 0:
        n+=i
    elif i%3 == 0:
        n+=i
print("2와 3의배수의 합:",n)

# 01-08 데이터구조(Dictionary, set), tuple(list comprehension)

list1 = [1, 2, 3, 4, 5]
print("list1: ",list1)

tuple1 = (1,2,3,4,5)
print("tuple1: ", tuple1)

# tuple은 아무것도 들어 있지 않은 값
a = 100, # ,표를 포함한 튜플이 된다.
print(a)
print(type(a))

# 1~10까지 숫자를 포함하는 튜플
values = [] # 리스트
for i in range(1, 10+1):
    values.append(i)
print(values)

values2 = () # 튜플은 append가 안된다. immutable 속성
# for i in range(1, 10+1):
#     values2.append(i)
# print(values)

values2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lists = []

for i in values2:
    lists.append(i)
print("튜플:",values2)
print("리스트:",lists)
print()
# 펑션활용 list(), tuple()
tuple_1_to_10 = tuple(range(1, 10+1))
print("튜플: ",tuple_1_to_10)

list_1_to_10 = list(tuple_1_to_10)
print("리스트",list_1_to_10)

my_info = [('이름','한빛'), ('이메일','hanbit@gamil.com'), ('연락처','010-1111-2222'), ('나라','korea')]

#튜플리스트
print("튜플 리스트",my_info)

for el in my_info:
    print(el[0], end=" : ")
    print(el[1])

# Dictionary 사전 키와 값을 가진 구조 mutable하다.
d = {}
print("Dictionary type: ",type(d))
d['name'] = 'han'
print(d)
print(d['name'])
d = {
    'name' : 'hansol',
    'phone' : '010-1234-1234',
    'nickname' : 'light',
    'age' : 29
}
print(d)
print(d['name'])
print(d.get('age'))
city = d.get('city')
print(city)

# Dictionary 순서가 보장되징낳는다.
myprofile = {
    '이름' : 'hansol',
    '나이' : '29',
    '연락처' : '010-2222-3333'
}

print(myprofile)

myprofile['이메일'] = 'hansol@naver.com'

for el in myprofile:
    print(el, end= ":")
    print(myprofile[el])

print("\n키값만 가져오기") # values()
for el in myprofile.values():
    print(el)

for el in myprofile:
    print("\n get \n",myprofile.get(el))

print("튜플 필요시") # items():
for el in myprofile.items():
    print(el)

# my_info = [('이름','한빛'), ('이메일','hanbit@gamil.com'), ('연락처','010-1111-2222'), ('나라','korea')]
my_info_dic ={}

# for el in my_info:
#     my_info_dic[el[0]] = el[1]

# print("my_info_dic: ",my_info_dic)
# my_info_dic: {'이름': '한빛', '이메일': 'hanbit@gamil.com', '연락처': '010-1111-2222', '나라': 'korea'}
print("dict 펑션: ",dict(my_info)) # 복잡하게 안해도 딕셔너리 변환 가능

m_info = [('nickname', 'icis'),('country','korea'), ('name','minjoong')]
print("m_info: ",dict(m_info))


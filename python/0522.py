#01-09 데이터구조

csv_values = """이름, 연락처, 나이, 이메일
    철수, 010-1234-1234,23,chulsu@gmail.com
    영희, 010-4321-4321, 30, Oh@gmail.com
    """

print("csv_values\n",csv_values)

# '\n'기준으로 나누는 함수
csv_values = csv_values.strip('\n') # 비어있는 스트링 지우기
csv_list = csv_values.split('\n')
print("csv_list\n",csv_list)

# strip 불필요한 단어 제거
string = "-------Python!!!--------"
print(string.strip('-'))

# string을 쪼개기
print("split으로 쪼개기:")
for el in csv_list:
    print(el.split(','))


keys = []

for el in csv_list[0].split(','):
    keys.append(el.strip(' '))

# print(keys)
# ['이름', '연락처', '나이', '이메일']

result=[]
for val in csv_list[1:]:
    result_dict ={}
    i = 0
    for el in val.split(','): # ','로 나누고
        result_dict[keys[i]]= el.strip(' ') # ' '띄어쓰기 제거
        i+=1
    result.append(result_dict)
print(result)
# [{'이름': '철수', '연락처': '010-1234-1234', '나이': '23', '이메일': 'chulsu@gmail.com'}, {'이름': '영희', '연락처': '010-4321-4321', '나이': '30', '이메일': 'Oh@gmail.com'}]

# set
set1 = {1, 2, 3, 4,4, 4, 5, 5}
print(set1)
set2 = {}
print(type(set2))
set2 = set()
print(set2)

set2.add(3)
set2.add(4)
set2.add(5)
set2.add(6)
set2.add(6)
print(set2)
# 두 dictornay 합치기
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))

# set1 변수에 1~100까지 숫자중 3의 배수

set1 = set()
set2 = set()
set3 = set()

for i in range(1, 100+1):
    # set3 변수에 1~100까지 숫자중 15의 배수
    if i%3 == 0:
        set1.add(i)
    # set2 변수에 1~100까지 숫자중 5의 배수
    if i %5 ==0:
        set2.add(i)
    # 15의 배수
    # if i % 15 == 0:
    #     set3.add(i)
    # 두 set1, set2에서 겹치는 숫자를 출력
    set3 = set1.intersection(set2) # set1과 set2의 공통된 부분을 set3에 넣어준다.

print("3의 배수:",set1)
print("5의 배수:",set2)
print("15의 배수:",set3)
# set3에서 set1에 포함되지 않는 숫자를 출력하세요. 없다.
print("set3.difference(set1)") # 공통값은 제외하고 출력시 difference set3-set1도 같은 결과


a = []
for i in range(1, 10+1):
    a.append(i**2)

print(a)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a = [i**2 for i in range(1,10+1)]
print(a)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

result = []
for i in range(1, 2+1):
    el = []
    for j in range(1, 2+1):
        el.append(j)
    result.append(el)

print(result)
# [[1, 2], [1, 2]]

# 변수를 사용하지 않은 경우 i 대신 _사용할 수 있다.
result =[[x for x in range(1, 3+1)] for _ in range(2)]
print(result)
# [[1, 2, 3], [1, 2, 3]]

# List Comprehension
# 1~100까지 숫자중 3의 배수인 숫자만 가진 리스트만들기
resultset = [x for x in range(1,100+1) if x % 3 == 0 ]
print("1~100까지 숫자중 3의 배수 리스트:\n",resultset)

# [[1,2,3],[1,2,3],[1,2,3]] 리스트 만들기
resultset = [[x for x in range(1, 3+1)] for _ in range(3)]
print("[1,2,3]*3 리스트 만들기\n",resultset)


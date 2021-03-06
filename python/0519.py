# 01-04~05-타입과 연산(Numbers, String, boolean), 데이터 구조(List)
b=["p","y","t","h","o","n"] # b
print(b)
# ['p', 'y', 't', 'h', 'o', 'n']
b[0]
print(b[0])
#'p'
b[0] = "j"
print(b)
# ['j', 'y', 't', 'h', 'o', 'n’]

print("Python" [0]) # P
print("Python" [-1]) # n
print("Python" [0:3]) #Pyt
print("Python" [0:4]) # Pyth
print("Python" [:]) # Python
print("Python" [0:len("python")]) # Python
var = "Python is Good!"
print(var[0:6]) # Python
print(var[7:9]) # is
print(var[0:9:1]) # 1씩증가, Python is
print(var[0:9]) # Python is
print(var[0:9:2]) # 2씩 증가 , Pto s
print(var[0:9:3]) # Ph
numbers = "0123456789"
print(numbers[::2]) # 02486 2씩 증가

likes = "치킨, 고양이, 씨리얼"
likes
# '치킨, 고양이, 씨리얼'
likes += ", 사과"
print(likes)
# '치킨, 고양이, 씨리얼, 사과'
print(likes[0:2])
# '치킨'
print(likes[0:1])
# '치'

print(likes[4:8])
# '고양이,'
print(likes[4:7])
# '고양이'
print(likes[9:12])
# '씨리얼'

a=[1,2.3, "String", 2, 3]
print(a)
# [1, 2.3, 'String', 2, 3]
print(a[0])
# 1
print(a[1])
# 2.3
print(a[-1])
# 3
print(a[:])
# [1, 2.3, 'String', 2, 3]
print(a[:-1])
# [1, 2.3, 'String', 2]
print(a[1:-1])
# [2.3, 'String', 2]
print(a[1:-1:2])
# [2.3, 2]

# input은 스트링 타입
name = input("이름을 입력하세요! ") 
age = input("나이를 입력하세요! ") 
phone = input("핸드폰 번호를 입력하세요! ")

print("당신의 이름은", name,"입니다", end=" ")
print("당신의 이름은", len(name),"글자입니다.")
print("당신의 나이는" +age+"살 입니다.")
print("당신의 연릭처는"+phone + "입니다.")

# 스트링 타입
print("안녕하세요 {name}씨, 좋은 {time}입니다.".format(name="로이", time="저녁"))

# mutable 수정 가능 immutable 수정불가능
# String은 immutable 수정불가능

# 빈 리스트 생성
likes = []
# 리스트 추가하는 법 append
likes.append('Python')
likes.append('cats')
likes.append('judo')
print(likes)
print(likes[0])
print(likes[1])
print(likes[2])
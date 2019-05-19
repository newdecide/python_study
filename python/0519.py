# 타입과 연산
b=["p","y","t","h","o","n"] # b
print(b)
# ['p', 'y', 't', 'h', 'o', 'n']
b[0]
print(b[0])
#'p'
b[0] = "j"
print(b)
# ['j', 'y', 't', 'h', 'o', 'n’]

print("Python" [0])
# 'P'
print("Python" [-1])
#'n'

print("Python" [0:3])
#'Pyt'
print("Python" [0:4])
#'Pyth'
print("Python" [:])
# 'Python'
print("Python" [0:len("python")])
# 'Python'
var = "Paython is Good!"
print(var[0:6])
# 'Paytho'
print(var[7:9])
#' i'
print(var[0:9:1]) # 1씩증가
# 'Paython i'
print(var[0:9])
# 'Paython i'
print(var[0:9:2]) # 2씩 증가
# 'Pyhni'
print(var[0:9:3])
# 'Ptn'
numbers = "0123456789"
print(numbers[::2])
# '02468'

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

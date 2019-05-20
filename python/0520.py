# 스트링 타입
print("안녕하세요 {name}씨, 좋은 {time}입니다.".format(name="로이", time="저녁"))

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
print(var[0:9:2]) # 2씩 증가 , Pyo s
print(var[0:9:3]) # Ph 
numbers = "0123456789"
print(numbers[::2]) # 02486 2씩 증가

# mutable 수정 가능 immutable 수정불가능
# String은 immutable 수정불가능

# 빈 리스트
likes = []
# 리스트 추가하는 법
print(likes.append('Python'))
print(likes.append('cats'))
print(likes.append('judo'))

print(likes)

print(likes[0])
print(likes[1])
print(likes[2])

# del, pop, append, reverse, sort()

# 리스트 복사: 주소를 가지고 있어 공유하면 같이 변경되게 된다, 병합,
# copy 하면 값이 변경되도 같이 ㅂ녀경되지 않는다.
# 참거짓 타입

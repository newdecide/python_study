# 01-12 파일 입출력 open 함수

# f = open('파일경로', '모드')
# f.close()

# write모드 파일 전체쓰기
# read모드 파일 읽는 모드
# append모드 파일 내용 추가하는 모드

# \n 줄바꿈 \t 탭

# print("안녕하세요. \n줄바꿀겁니다.")
# print("반갑습니다. \t탭했어요.")

# f = open("./hello.txt", "w")
# f.write("Hello World!")
# f.close()

f = open("/Users/odongju/Desktop/python_study/python/hello.txt", "r")
# 파일 내용 추가시
# for i in range(2, 10+1):
#     content = str(i) + "번째 줄입니다.\n"
#     # f.write(content)

# 파일 읽을때
# content = f.read() # f.write()
content = f.readline() # 한줄씩 불러 온다.
print(content)
print(f.readline())
print(f.readline())
# print(content)
# f.seek(0) # 커서 이동
# print(f.read())
# f.close

# pwd 현재위치 파악할 수 있다.

# f = open("./hello2.txt", "w")
# f.write("Hello World!")
# f.close()

# 1) 파일을 만들어서 "hello world!"를 10줄 써 넣으세요.
f2 = open("./hello2.txt","r") # w 쓰기, a 추가 r 읽기
for _ in range(10):
    # f2.write("hello world!\n") # 글쓰기
# 2) 파일을 append 모드로 열어서 "hellp python!"을  10줄 추가하세요.
    # f2.write("hello pyhthon! \n") # 글추가
    print(f2.readline())
f2.seek(0)
print(f2.read())
f2.close

# 3) 파일을 읽어 온 뒤에 파일내용에 hello world를 20번 hello python을 10번 출력해보세요

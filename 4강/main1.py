hello = "안녕하세요! 오늘은 기분이 좋습니다."
print(hello[5])
hello = '"안녕" 철수가 인사를 했다.'
print(hello[9])
hello = 'Life is too short. You need Python'
print(hello[4])
A = 472
B = 385
print(A*5)
print(A*8)
print(A*3)
print(A*B)
A = 5
B = 8
C = 4
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
print(A-C, A%C, B%C, C//B)
#hello = "안녕하세요!"
#print(hello[5])
#print(hello[-1])
a = 'Life is too short, You need Python'
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])
number = '24가 1234'
print(number[-4:])
a = '우리 강아지 이름은 초코입니다.'
print(a[11:13])
a = "3"
b = "4"
print(a+b)
a = 3
b = 4
print(a+b)
print("Hi" * 3)
print("Hi " * 3)
print("-" * 80)
s1 = "python"
s2 = "java"
s3 = s1 + ' ' + s2 + ' '
print(s3 * 4)
s1 = '좋은 아침 입니다!'
s2 = s1[0:5] + s1[-1]
print(s2)
number  = 3
destination = "학교"
print("나는 사과 %d개를 먹었다. 그리고 %s에 갔다." % (number, destination))
print("나는 사과 %d개를 먹었다." % 5)
print("나는 사과 %s개를 먹었다" % "다섯")
s = "나는 사과 %d개를 먹었다"
print(s % 1000)
num = 1000
print(s % num)
def add(a, b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)
print(add(10, 15))
print(add(2345889, 194943))
print(add(3, 100000000000))
def minus(a, b):
    return a - b
print(minus(a, b))
name1 = "김철수"
age1 = 10
name2 = "홍길동"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
print("이름: {0} 나이: {1}" . format(name1, age1))
print("이름: {0} 나이: {1}" .format(name2, age2))
def plus(a, b):
    return a + b
def multi(a, b):
    return a * b
def divi(a, b):
    return a//b
a = 6
b = 3
print(plus(a, b))
print(minus(a, b))
print(multi(a, b))
print(divi(a, b))
#def hello():
#    print("안녕하세요")
#hello()
hello()
def hello():
    print("Hi")

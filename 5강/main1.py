#def hello():
#    print("안녕하세요")
#hello()
#hello()
def hello():
    print("Hi")
def message():
    print("A")
    print("B")
message()
print("C")
message()
def say1(name):
    string = '안녕하세요? ' + name + '님'
    return string
def say2(name):
    string = '안녕하세요? ' + name + '님'
    print(string)
name = "홍길동"
say1(name)
say2(name)
string = say1(name)
print(string)
def plus(a, b):
    return a+b
def minus(a, b):
    return a-b
def multi(a, b):
    return a * b
def divi(a, b):
    return a//b
a = 6
b = 3
print(plus(b, a))
print(minus(b, a))
print(multi(b, a))
print(divi(b, a))
def hi():
    print('안녕, 함수!')
hi()
print('함수 한 번 출력')
hi()
print('함수 두 번 호출')
hi()
hi()
print('함구 다섯 번 호출')
hi()
hi()
hi()
hi()
hi()
print('함수 호출 끝')
def add(a, b):
    result = a + b
    print("{} + {} = {}".format(a,b,result))
add(10,5)
#name = input('당신의 이름은? ')
#print(name)
def add_10(a):
    return(a + 10)
print(add_10(4))
#print('당신의 이름은? ')
#name = input()
#print(name)
#name = input('당신의 이름은? ')
#age = int(input('당신의 나이는? '))
#print('당신은 ' + name + '이고 ' + str(age) + '살입니다. ')
#print('당신은', name, '이고 ', age, '살입니다. ')
#print('당신은 {}이고 {}살 입니다.'.format(name, age))
#print('내년에 ' + str(age + 1) +'살입니다. ')
#print('가위 바위 보 중 하나를 내주세요> ')
#mine = input()
#print('mine:', mine)
#mine = input('가위 바위 보 중 하나를 내주세요> ')
#print('mine:', mine)
#date = input('오늘 날짜 : ')
#year = date[0:4]
#month = date[5:7]
#day = date[8:10]
#print('년 :', year)
#print('월 :', month)
#print('일 :', day)
def print_with_smile(a):
    print(a + ":D")
print_with_smile("hi")
def print_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
print_operation(2, 4)

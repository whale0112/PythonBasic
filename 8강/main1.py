for number in range(1, 21, 1):
    print(number)
for number in range(10, 101, 1):
    print(number)
#max = int(input())
#for number in range(0, max+1, 1):
    #print(number)
#print("숫자 두 개를 작은수부터 입력해주세요.")
#min = int(input())
#max = int(input())
#for number in range(min, max+1, 1):
    #print(number)
#max = int(input())
#for number in range(1, max+1, 3):
    #print(number)
number = 1
while number <= 1000:
    print(number)
    number = number + 1
for number in range(1, 1001, 1):
    print(number)
for number in range(1, 10):
    string = '{}x{}={}'.format(2, number, 2 * number)
    print(string)
for number in range(1, 1001, 1):
    if number % 3 == 0:
        print(number)
for number in range(1, 10, 1):
    string = '{}x{}={}'.format(3, number, 3 * number)
    print(string)
for number in range(1, 10, 2):
    string = '{}x{}={}'.format(3, number, 3 * number)
    print(string)
for 단 in range(2, 10):
    for number in range(1, 10):
        string = '{}x{}={}'.format(단, number, 단 * number)
        print(string)
num = 0
for count in range(1, 11):
    num = num + count
print(num)
for 단 in range(2, 10):
    print('{}단 시작'.format(단))
    for number in range(1, 10):
        string = '{}x{}={}'.format(단, number, 단 * number)
        print(string)
    print('{}단 종료'.format(단))
#시작단 = int(input('구구단 시작 단을 입력하세요(1~9):'))
#끝단 = int(input('구구단 끝 단을 입력하세요(1~9):'))
#for 단 in range(시작단, 끝단+1):
    #for number in range(1, 10):
        #string = '{}x{}={}'.format(단, number, 단 * number)
        #print(string)
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
a = 0
while a < 10:
    a = a + 1
    if a == 5:
        print('{}입니다.'.format(a))
        break
    print(a)
num = 0
for count in range(1, 11, 2):
    num = num + count
print(num)
num = 1
for count in range(1, 11):
    num = num * count
print(num)
for i in range(1, 6):
    print("*" * i)
for i in range(5, 0, -1):
    print("*" * i)
#max = int(input())
#for i in range(1, max+1):
    #print("*" * i)
for i in range(1, 11):
    print(i)
for i in range(10):
    print(i)
for i in range(10, 0, -1):
    print(i)
while True:
    score = int(input('점수: '))
    if score == -1:
        break
    elif score >= 60:
        print("합격")
    else:
        print("불합격")
while True:
    cap = input('한국의 수도는? : ')
    if cap == '그만':
        break
    elif cap == '서울':
            print("정답입니다.")
    else:
        print("틀렸습니다.")

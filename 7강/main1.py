hit = 0
while hit < 10:
    hit = hit + 1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 10:
        print("나무가 넘어갔습니다.")
    elif hit == 8:
        print("나무가 곧 넘어갈것 같습니다.")
#주민번호 = input("주민등록번호: ")
#print(주민번호[7:8])
#print(주민번호[8])
#if 주민번호[7] == "1" or 주민번호[7] == "3":
    #print("남자")
#elif 주민번호[7] == "2" or 주민번호[7] == "4":
    #print("여자")
#else:
    #print("오류")
#prompt = """
#100을 입력하면 종료가 되는 프로그램입니다.
#100. 종료
#Enter number: """
#number = 0
#while number != 100:
    #print(prompt)
    #number = int(input())
number = 10
while number <10:
    number = number +1
    print(number)
number = 11
while number <= 10:
    print(number)
    number = number + 1
number = 100
while number < 100:
    number = number + 1
    print(number)
number = 101
while number <= 100:
    print(number)
    number = number + 1
#number = 0
#max = int(input())
#while number < max:
    #number = number + 1
    #print(number)
#while 3<5:
    #rint("3은 5보다 작다")
if 3<5:
    print("3은 5보다 작다")
#print("숫자 두 개를 작은수부터 입력해주세요.")
#min = int(input())
#max = int(input())
#while min <= max:
    #print(min)
    #min = min + 1
def getGrade(score):
    if 81 <= score <= 100:
        print("grade is A")
    elif 61 <= score <= 80:
        print("grade is B")
    elif 41 <= score <= 60:
        print("grade is C")
    elif 21 <= score <= 40:
        print("grade is D")
    elif 0 <= score <= 20:
        print("grade is E")
    else:
        print("오류")
getGrade(94)
number = 0
while number < 5:
    number = number + 1
    print(number)
number = 0
while number <= 6:
    if number < 3:
        number = number + 1
    else:
        print(number)
        number = number + 1
for number in range(1, 21, 1):
    print(number)
for number in range(10, 101, 1):
    print(number)
#max = int(input())
#for number in range(0, max + 1, 1):
    #print(number)
#print("숫자 두 개를 작은수부터 입력해주세요.")
#min = int(input())
#max = int(input())
#for number in range(min, max + 1, 1):
    #print(number)
for number in range(1, 10):
    string = '{}x{}={}'.format(9, number, 9 * number)
    print(string)
#단 = int(input('구구단을 출력합니다. 몇 단인지 입력해주세요'))
#for number in range(1, 10):
    #string = '{}x{}={}'.format(단, number, 단 * number)
    #print(string)
for number in range(1, 11, 1):
    print(number)
for number in range(3, 7, 1):
    print(number)
    print("-------")

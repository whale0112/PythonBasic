list = [1, 5, 3, 6]
print(list[-1])
list = [1, 5, 3, 6]
print(list[1:3])
print(list[2:])
print(list[:2])
과목 = ['국어', '수학', '영어', '과학']
print(과목)
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color))
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
last_color = rainbow[6]
print('무지개의 마지막 색은 {}이다'.format(last_color))
list = [1, 5, 3, 6]
list.append(8)
print(list)
list = [1, 5, 3, 6]
list.insert(2, 4)
print(list)
list = [1, 5, 3, 6]
list.insert(3, 7)
print(list)
#while True:
    #a = int(input('숫자를 입력하세요'))
    #if a == -1:
        #break
    #elif a % 7 == 0:
        #print('7의 배수 입니다')
    #else:
        #print('7의 배수가 아닙니다')
list = [1, 2, 3]
list.append(4)
print(list)
list = [1, 2, 3, 5]
list.insert(3, 4)
print(list)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)
list = [1, 2, 3]
del list[1]
print(list)
list = [1, 2, 3]
list.remove(2)
print(list)
list = [1, 2, 3]
list[1] = 10
print(list)
#while True:
    #score = int(input('점수: '))
    #if score == -1:
        #break
    #elif 81 <= score <= 100:
        #print('A등급')
    #elif 61 <= score <=80:
        #print('B등급')
    #elif 41 <= score <= 60:
        #print('C등급')
    #elif 21 <= score <= 40:
        #print('D등급')
    #lif 0 <= score <= 20:
        #print('E등급')
    #else:
        #print('오류')
#t1 = (1, 2, 'a', 'b')
#del t1[0]
#t1 = (1, 2, 'a', 'b')
# t1[0] = 'c'
음식 = ('떡볶이', '햄버거', '피자', '김밥')
print(음식)
rainbow = ('빨강', '주황', '노랑', '초록', '파랑', '남색', '보라')
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color))
last_color = rainbow[6]
print('무지개의 마지막 색은 {}이다'.format(last_color))
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t * 10)
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t2 = t * 10
print(t2)
print(len(t2))
#while True:
    #title = '''
    #구구단 프로그램을 실행합니다.
    #1. 홀수 구구단
    #2. 짝수 구구단
    #3. 종료'''
    #a = int(input(title))
    #if a == 1:
        #for number in range(1, 10, 2):
            #for number2 in range(1, 10, 1):
                #print('{}x{}={}'.format(number, number2, number*number2))
        #break
    #elif a == 2:
        #for number in range(2, 10, 2):
            #for number2 in range(1, 10, 1):
                #print('{}x{}={}'.format(number, number2, number*number2))
        #break
    #elif a == 3:
        #break
    #else:
        #continue
my_variable = []

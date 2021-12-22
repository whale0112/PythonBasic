class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('{}가 먹는다'.format(self.name))
    def move(self):
        print('{}가 움직인다'.format(self.name))
class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner
    def bark(self):
        print('멍멍')
    def shake(self):
        print('{}가 꼬리를 흔든다'.format(self.name))
    def __str__(self):
        sentence = '이름:{}, 나이:{}, 주인:{}'.format(self.name, self.age, self.owner)
        return sentence
dog = Dog('코코', 2, '홍길동')
print(dog)
dog.eat()
class Animal:
    def __init__(self, age):
        self.age = age
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.name = name
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def __str__(self):
        sentence = '이름:{}, 나이:{}'.format(self.name, self.age)
        return sentence
dog = Dog('코코', 2)
print(dog)
dog2 = Dog('두리', 5)
print(dog2)
dog3 = Dog('먼지', 7)
print(dog3)
class Animal:
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')
class Dog(Animal):
    def eat(self):
        print('강아지가 밥을 먹는다')
    def move(self):
        print('강아지가 몸을 움직인다')
class Bird(Animal):
    def eat(self):
        print('새가 모이를 먹는다')
    def move(self):
        print('새가 몸을 움직인다')
animal = Animal()
animal.eat()
animal.move()
dog = Dog()
dog.eat()
dog.move()
bird = Bird()
bird.eat()
bird.move()
class Duck(Animal):
    def eat(self):
        print('오리가 밥을 먹는다')
    def move(self):
        print('오리가 몸을 움직인다')
duck = Duck()
duck.eat()
duck.move()
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def 먹기(self):
        print('먹는다')
    def 잠자기(self):
        print('잠잔다')
    def 쉬기(self):
        print('쉰다')
class Student(Human):
    def __init__ (self, name, age, 학년):
        super().__init__(name, age)
        self.학년 = 학년
    def 공부하기(self):
        print('공부합니다.')
    def __str__(self):
        sentence = '이름:{}, 나이:{}, 학년:{}'.format(self.name, self.age, self.학년)
        return sentence
student = Student('홍길동', 12, 5)
student.먹기()
student.잠자기()
student.쉬기()
student.공부하기()
print(student)
student1 = Student('성춘향', 13, 6)
student2 = Student('이몽룡', 11, 4)
print(student1)
print(student2)
class Human:
    def __init__(self, name, age, 성별, 전화번호, 취미):
        self.name = name
        self.age = age
        self.성별 = 성별
        self.전화번호 = 전화번호
        self.취미 = 취미
    def 먹기(self):
        print('먹는다')
    def 잠자기(self):
        print('잠잔다')
    def 쉬기(self):
        print('쉰다')
class Student(Human):
    def __init__ (self, name, age, 성별, 전화번호, 취미, 학년, 학교, 반, 좋아하는_과목):
        super().__init__(name, age, 성별, 전화번호, 취미)
        self.학년 = 학년
        self.학교 = 학교
        self.반 = 반
        self.좋아하는_과목 = 좋아하는_과목
    def 공부하기(self):
        print('공부합니다.')
    def __str__(self):
        sentence = '이름:{}, 나이:{}, 학년:{}'.format(self.name, self.age, self.학년)
        return sentence
class Teacher(Human):
    def __init__(self, name, age, 성별, 전화번호, 취미, 담당학년):
        super().__init__(name, age, 성별, 전화번호, 취미)
        self.담당학년 = 담당학년
    def 수업하기(self):
        print('수업한다')
teacher = Teacher(1, 2, 3, 4, 5, 6)
teacher.먹기()
teacher.수업하기()

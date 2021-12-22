from main1 import *
dog = Dog()
dog.eat()
import random

for i in range(6):
    number = random.randint(1, 45)
    print(number, end=' ')
import time
current = time.ctime()
print(current)
list_cur = current.split(' ')
print(list_cur)
for t in list_cur:
    print(t)

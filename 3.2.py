from random import randint

a=randint(1, 10)
b=randint(1, 10)
if a<b:
    for x in range(b-a+1):
        print(x+a)
else:
    for x in range(a-b+1):
        print(x+b)

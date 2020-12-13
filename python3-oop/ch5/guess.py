import random

real = random.randint(0, 100)

for i in range(5):
    a = int(input("Please input a number:"))
    if a > real:
        print('Sorry, it is too lager')
    elif a < real:
        print("Sorry, it is too small")
    else:
        print("Yes")
        break
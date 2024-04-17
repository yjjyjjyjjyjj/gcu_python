import random

x=random.randint(1,100)
y=random.randint(1,100)

if random.randint(1,2) == 1:
    answer = int(input(f"{x} + {y} = "))
    flag = (answer == (x+y))
else:
    answer = int(input(f"{x} - {y} = "))
    flag = (answer == (x-y))

print(flag)
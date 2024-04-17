import math

x1 = int(input("x1 입력 : "))
y1 = int(input("y1 입력 : "))
x2 = int(input("x2 입력 : "))
y2 = int(input("y2 입력 : "))

base = (x1-x2)**2
height = (y1-y2)**2

hypotenuse = math.sqrt(base+height)

print("두 좌표 사이의 거리는",hypotenuse)
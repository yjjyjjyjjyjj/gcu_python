def getSorted(x,y):
    if y<x:
        temp = y
        y = x
        x = temp

    return x, y

numA = int(input("첫 번째 정수: "))
numB = int(input("두 번째 정수: "))

x,y = getSorted(numA, numB)
print(f"({x}, {y})")
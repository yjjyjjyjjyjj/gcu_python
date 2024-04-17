def findMaximunGongYakSu (a, b):
    maximunGongYakSu = 0
    compareNum = a if a<=b else b
    for i in range(1, compareNum+1):
        if(numA %i ==0) and (numB %i == 0):
            maximunGongYakSu = i
    return maximunGongYakSu

numA = int(input("첫 번째 정수: "))
numB = int(input("두 번째 정수: "))

print(findMaximunGongYakSu(numA, numB))

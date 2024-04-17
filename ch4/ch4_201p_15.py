result = float(0)   #flaot 형 선언
for i in range(1, 101, 2):  #1부터 2씩 증가
    result += i/(i+2) #ex 1/(1+2)

print(result)
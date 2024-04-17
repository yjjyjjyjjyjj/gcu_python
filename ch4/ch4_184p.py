import random

sum = 0 #횟수를 세는 변수
for i in range(0, 1000):
   a = random.randint(1,6)  #첫번째 주사위
   b = random.randint(1,6)  #두번째 주사위
   if (a+b) == 6:   #첫번째 + 두번째 더한 값이 6인 것을 확인
       sum+=1       #횟수에 추가

print("6이 나온 횟수:",sum)
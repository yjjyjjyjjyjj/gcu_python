# https://ko.wikihow.com/Pi-%EA%B3%84%EC%82%B0%ED%95%98%EB%8A%94-%EB%B2%95

# phi = 3.0
# signFlag = True  #true면 +, False면 - initilize는 True
# startNum = 2
#
# # loopCnt = int(input("반복 횟수를 입력하세요. : "))
#
# for i in range(0,300):
#     if signFlag == True:
#         phi += 4/(startNum*(startNum+1)*(startNum+2))
#         signFlag = False
#     else:
#         phi -= 4/(startNum*(startNum+1)*(startNum+2))
#         signFlag = True
#     startNum = startNum+2
#
# print("%.300f" % phi)

from decimal import *
getcontext().prec = 300     #n자리 숫자까지 출력되도록 하는 설정 값

result = Decimal(3.0)       #Decimal 자료형으로 변수를 선언한다.
op = 1                      #+- 부호

for n in range(2, 2*300+1, 2):  #공식의 n이 2만큼 증가하므로 2씩 올라가게한다.
    result += 4/Decimal(n*(n+1)*(n+2)*op)
    op *= -1

print(result)
n = int(input("n의 값을 입력하시오: "))     #n값 입력받기
result = 0      #n²합 변수 초기화

for i in range(1, n+1):
    result += i**2  #result 변수에 i² 한 값 더하기

print("계산값은 %d입니다." % result)
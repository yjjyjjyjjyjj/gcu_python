num = int(input("정수를 입력하시오: "))

print("약수:",end=" ")

for i in range(1, num+1):
    if(num%i == 0):   #입력받은 정수와 i를 나눈 값의 나머지가 0이면 입력받은 정수의 약수이다.
        print(i, end=" ")   #약수 출력
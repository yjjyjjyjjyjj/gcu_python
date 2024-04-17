n = int(input("4자리의 숫자 입력: "))

sum = 0

sum += n%10;
sum += n//10%10
sum += n//10//10%10
sum += n//10//10//10

print("각 자리의 숫자 합은", sum)
yun = int(input("연도를 입력하시오: "))

if (yun%4 == 0 and yun%100 !=0) or yun%400==0:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")
a=int(input("삼각형의 첫번째 각을 입력하세요.: "))
b=int(input("삼각형의 두번째 각을 입력하세요.: "))
c=int(input("삼각형의 세번째 각을 입력하세요.: "))

if(a+b+c) == 180:
    print("올바른 삼각형입니다.")
else:
    print("올바르지 않은 삼각형입니다.")
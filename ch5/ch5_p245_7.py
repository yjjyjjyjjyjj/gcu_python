def sub(a=2, b=3):
    print(a, b)

sub()
sub(a=10)
sub(5, 6)
sub(b=10)

# 함수에 a,b의 디폴트 값이 정의 되어있기때문에 함수를 호출할때 인자로 아무것도 넣지 않거나, 일부만 인자를 넣으면
# 함수에서 디폴트 값을 사용한다.
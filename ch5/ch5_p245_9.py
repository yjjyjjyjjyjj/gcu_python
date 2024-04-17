global=0

def sub():
    local=1
    print(global)
    print(local)

sub()
print(global)
print(local)

'''
1째 줄의 전역변수 global은 예약어이며 이코드가 돌아가도록 하려면 global이 아닌 다른 변수명으로 선언하여야한다.
global문은 지역변수 인데 전역 변수로 사용하고 싶을때 사용한다.
그리고 10번째 줄 local은 함수내에서 만 쓰이는 지역 변수이므로 함수 밖에서는 오류가 발생한다.
'''
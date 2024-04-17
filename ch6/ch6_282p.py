salaries = [200, 250, 300, 280, 500]

def modify(values, factor):
    for e in values:
        print(e)
        e = e*factor

print("인상전", salaries)
modify(salaries, 1.3)
print("인상후", salaries)

'''
실행 결과

인상전 [200, 250, 300, 280, 500]
인상후 [200, 250, 300, 280, 500]

e는 values 값을 참조하여 변수에 담았기 때문에 e에 값을 집어넣는게 아닌
value에 값을 집어넣어야 정상적으로 출력이 된다.
'''
n = 1  # 변수 초기화
while True:
    if n ** 2 > 500:    #n²이 500 이상이면 while문 탈출
        break
    else:
        n += 1          #n²이 500 이하이면 n에 1더하기

print("n² > 500 중 가장 작은 n은 %d입니다." % n)

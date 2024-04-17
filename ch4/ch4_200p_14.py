for i in range(2, 20+1):    #2부터 20까지 반복
    isSosu = True   #반복문 돌때마다 소수인지 확인하는 Flag
    for j in range(2,i): #j는 i-1까지 돌아간다. 그중에 한개의 숫자라도 나눈 나머지가 0이되면 Flag가 False로 바뀐다.
        if i%j == 0:
            isSosu = False
            break
    if isSosu == True:  #Flag에 따라 소수 출력
        print(i, end=" ")
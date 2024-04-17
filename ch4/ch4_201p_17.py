for i in range(0,10): #i = 0~9
    if i%3 == 0 and i%5 == 0:   #i를 3, 5로 나눈 나머지가 둘다 0이면
        print("fizzbuzz")
    elif i%3 == 0 and i%5 != 0: #i를 3으로 나눈 나머지가 0이고 5로 나눈 나머지가 0이 아니면
        print("fizz")
    elif i%3 != 0 and i%5 == 0: #i를 3으로 나눈 나머지가 0이 아니고 5로 나눈 나머지가 0이면
        print("buzz")
    else:                       #i를 3, 5로 나눈 나머지가 둘다 0이 아니면
        print("*")
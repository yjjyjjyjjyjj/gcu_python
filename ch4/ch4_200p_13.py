hang = int(input("몇 번째 항까지 구할까요? "))

n1 = 0  #더할 첫번째 수 초기화
n2 = 1  #더할 두번째 수 초기화

fiboList = []   #수열을 저장하는 배열

for i in range(0, hang):
    fiboList.append(str(n1))    #str으로 넣는 이유는 후에 ,으로 배열을 합칠때 int형이면 합쳐지지 않기 때문이다.
    nTemp = n1 + n2
    n1 = n2
    n2 = nTemp

fiboList.append(str(n1))    #마지막에 값이 append 되지 않으므로, for문이 끝난후 한번더 n1을 넣어준다.
fiboListToStr = ", ".join(fiboList) #string 자료형의 배열의 값을 ", "로 묶어주는 역할을 한다.
print(fiboListToStr)
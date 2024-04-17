aList = [x+y for x in ['Hello ', 'Good '] for y in ['World', 'Bye']]
print(aList)

'''
각 반복문의 배열의 요소들이 추출되어 문자열 합치기 되어 하나의 리스트로 출력된다. 따라서 결과 값은
['Hello World', 'Hello Bye', 'Good World', 'Good Bye'] 이다.
리스트 함축 방식으로 코드를 작성하면 코드가 간결해지는 효과가 있지만 다른 사람이 코드를 볼때 이해하기 힘들 수 있다.
'''
values = [1,2,3,4,5,6,7,8,9,10]
result = 0
for i in range(0, len(values),2):
    result = result + values[i]
print(result)

'''
for문에서 i가 2씩 올라간다. 따라서 0,2,4,6,8 인덱스가 조회되며, result값에 더해진다.
실행 결과는 25이다.
'''
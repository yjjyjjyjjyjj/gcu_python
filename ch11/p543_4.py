list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("원래 리스트:")
print(list1)

print("짝수:")
print(list(filter(lambda x: x % 2, list1)))
print("홀수:")

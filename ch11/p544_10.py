even_number = filter(lambda n: n%2 == 0, [1,2,3,4,5,6,7,8,9,10])
print(list(map(lambda n: n**2, even_number)))

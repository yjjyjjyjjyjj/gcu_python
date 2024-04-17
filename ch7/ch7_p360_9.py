str1 = input("첫 번째 문자열: ")
str2 = input("두 번째 문자열: ")

list =list(set(str1) & set(str2))

print("\n모두 포함된 글자: ", end="")
for i in list:
    print(i,end=" ")
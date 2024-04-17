list = list("Hello World123")

print("Hello World123 -> ", end="")

strLetterChk = {}

strLetterChk["LETTERS"] = sum(1 for x in list if x.isalpha())
strLetterChk["DIGITS"] = sum(1 for x in list if x.isdigit())

print(strLetterChk)
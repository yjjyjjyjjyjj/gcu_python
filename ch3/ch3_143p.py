print("========================")
print("메뉴 1번: 치즈 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("메뉴 4번: 코울슬로")
print("메뉴 5번: 제로콜라")
print("========================")

selection = int(input("메뉴를 선택하세요:"))

if selection >= 1 and selection <= 5 :
	print("메뉴 ", selection)
else :
	print("잘못 입력하셨습니다.")
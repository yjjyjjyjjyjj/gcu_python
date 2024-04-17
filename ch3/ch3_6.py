import random

sel=int(input("선택하시오(1:가위 2:바위 3:보)"))
comSel=random.randint(1,3)
print(f"컴퓨터의 선택(1:가위 2:바위 3:보) {comSel}")
isWin = 0

if sel==1:
    if comSel==1:
        isWin=0
    elif comSel==2:
        isWin=-1
    elif comSel==3:
        isWin=1
elif sel==2:
    if comSel==1:
        isWin=1
    elif comSel==2:
        isWin=0
    elif comSel==3:
        isWin=-1
elif sel==3:
    if comSel==1:
        isWin=-1
    elif comSel==2:
        isWin=1
    elif comSel==3:
        isWin=0
        
if isWin==0:
    print("비겼음")
elif isWin==1:
    print("사람이 이겼음")
elif isWin==-1:
    print("컴퓨터가 이겼음")
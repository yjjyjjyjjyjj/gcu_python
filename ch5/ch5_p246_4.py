def getGrade(score):
    if score >= 60 and score < 70:
        return "D"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 90:
        return "A"
    else:
        return "F"

score = int(input("점수를 입력하세요: "))

print(f"성적은 {getGrade(score)} 입니다")


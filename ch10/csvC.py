import csv

f = open('./weather.csv')
data = csv.reader(f)
header = next(data)
temp = 1000
for row in data:
    if temp > float(row[3]):
        temp = float(row[3])

print("가장 추웠단 날의 기온은", temp, "입니다.")
f.close()

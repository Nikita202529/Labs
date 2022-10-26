from datetime import datetime

f = open('textData.txt')
documentData = f.read()
arrData = documentData.split( )

dateArr = []
pressure = []
pressureDay = []

i = 0
while i < len(arrData):
    bool = 0
    if not(i % 2):
        str = arrData[i].replace('T', ' ')
        day = datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        j = 0
        while j < len(dateArr):
            if day.day == dateArr[j]:
                bool = 1
                break;
            j += 1
        if not(bool):
            dateArr.append(day.day)
    else:
        str = arrData[i].replace(',', '.')
        pressure.append(float(str))
        if len(pressure) == 24:
            pressureDay.append(pressure)
            pressure = []
    i += 1


# print('Массив дат')
# print(dateArr)
# print('Массив давления')
# print(pressureDay)


middle = []
EMAmiddle = []

for i in range(len(dateArr)):
    sum = 0
    for j in range(24):
        sum += pressureDay[i][j]
    middle.extend([round(sum/24, 1)])
    if i < 1:
        EMAmiddle.extend([round(sum/24, 1)])
    elif i > 0:
        EMAmiddle.extend([round(((sum / 24) * (2 / (1 + i)) + (EMAmiddle[i - 1] * (1 - (2 / (1 + i))))), 1)])

print('Массив среднесуточного давления')
print(middle)
print('Массив скользящего среднего давления')
print(EMAmiddle)

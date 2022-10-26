from datetime import datetime

# Читаем текстовый файл с данными
f = open('textData.txt')
# Сохраняем данные в переменную
documentData = f.read()
# Записываем данные в массив
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



print('Массив дат')
print(dateArr)
print('Массив давления')
print(pressureDay)

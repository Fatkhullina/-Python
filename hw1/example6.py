distance = float(input("Введите количество км в первый день:"))
max_distance = float(input("Введите необходимое количество км:"))
day = 1
while distance + distance * 10 / 100<= max_distance:
    day = day + 1
    distance = distance + distance * 10 / 100
else:
    day = day + 1
    print(f"Количество дней необходимое на преодоление дистанции равно {day}")
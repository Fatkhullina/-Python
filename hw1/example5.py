proceeds = float(input("Введите значение выручки:"))
cost = float(input("Введите значение издержек:"))
if proceeds>cost:
    number = int(input("Введите количество сотрудников:"))
    profitability = proceeds / number
    print(f"Положительная прибыль. Прибыль на одного сотрудника = {profitability}")
elif proceeds==cost:
    print("Нулевая прибыль")
elif proceeds<cost:
    print("Отрицательная прибыль")


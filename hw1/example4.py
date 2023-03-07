n = int(input("Введите целое положительное число:"))
# максимальное число
max_1 = n%10
while n>1:
    n = n//10
    if max_1<n%10:
            max_1 = n%10
    else: max_1 = max_1
print(f"Максимальное число:{max_1}")



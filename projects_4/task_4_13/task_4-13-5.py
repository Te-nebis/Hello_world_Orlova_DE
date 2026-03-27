N = int(input("Введите количество чисел N: "))

max = int(input("Введите число: ")) # Нужен max, чтобы с чем-то сравнивать значения в цикле

for i in range(1, N):
    num = int(input("Введите число: "))
    if num > max:
        max = num

print(max)
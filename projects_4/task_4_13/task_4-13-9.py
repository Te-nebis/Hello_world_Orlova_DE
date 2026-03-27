N = int(input("Введите количество элементов массива N: "))

total = 0

for i in range(N):
    num = int(input(f"Введите элемент {i+1}: "))
    if num % 2 != 0:
        total = total + num

print(total)
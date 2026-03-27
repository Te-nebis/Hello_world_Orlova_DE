N = int(input("Введите количество элементов массива N: "))

count = 0

for i in range(N):
    num = int(input(f"Введите элемент {i+1}: "))
    if num > 0:
        count = count + 1

print(count)
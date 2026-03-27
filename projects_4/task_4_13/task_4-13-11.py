N = int(input("Введите количество элементов массива N: "))

total_num = 0  
total_i = 0    

for i in range(N):
    num = int(input(f"Введите элемент {i+1}: "))
    if i % 2 == 0:  
        total_num = total_num + num  
        total_i = total_i + 1        

print(total_num / total_i)
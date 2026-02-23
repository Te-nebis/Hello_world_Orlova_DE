# Поле для введения последовательности и написание её в верхнем регисте
dna = input("Введите последовательность ДНК: ")
dna_main = dna.upper()

# Выведемпоследовательность в верхнем регистре 
print("\nПоследовательность в верхнем регистре:", dna_main)

# Подсчет каждого нуклеотида и вывод результата
count_A = dna_main.count("A")
count_T = dna_main.count("T")
count_G = dna_main.count("G")
count_C = dna_main.count("C")

print("\nПодсчет нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")

# Подсчет и вывод общей длины строки
dna_number = len(dna_main)
print("\nОбщая длина:", dna_number)

# Подсчет и вывод процентного содержания каждого нуклеотида
percent_A = count_A / dna_number * 100
percent_T = count_T / dna_number * 100
percent_G = count_G / dna_number * 100
percent_C = count_C / dna_number * 100

print("\nПроцентное содержание каждого нуклеотида")
print(f"A: {percent_A:.2f}%")
print(f"T: {percent_T:.2f}%")
print(f"G: {percent_G:.2f}%")
print(f"C: {percent_C:.2f}%")
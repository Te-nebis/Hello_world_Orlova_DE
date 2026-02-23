seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]

for name in seq:
    print(f"\nПоследовательность: {name}")
    print(f"Построчно:")

    for latter in name:
        print(latter)

print("Цикл выполнен")

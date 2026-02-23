capsules_number = int(input("Введите общее количество произведенных капсул: "))
capsules_per_package = int(input("Введите количество капсул в одной упаковке: "))
full_packs = capsules_number // capsules_per_package
remaining = capsules_number % capsules_per_package
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}\nОстаток капсул: \t{remaining}")
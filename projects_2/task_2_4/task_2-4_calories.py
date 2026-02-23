protein_mass = int(input("Введите массу белка в продукте:"))
fats_mass = int(input("Введите массу жиров в продукте:"))
carbohydrates_mass = int(input("Введите массу углеводов в продукте:"))
cal = protein_mass * 4 + fats_mass * 9 + carbohydrates_mass * 4
print(f"Общая калорийность продукта составляет {cal} г.")
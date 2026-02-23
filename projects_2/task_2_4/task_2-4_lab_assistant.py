solution_volume = float(input("Введите нужный объем раствора (мл): "))
salt_mass = solution_volume * 0.009
water_volume = solution_volume

print("\nОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:")
print("-" * 23)
print(f"Общий объем: {solution_volume} мл")
print(f"Масса соли:  {salt_mass:.2f} г")
print(f"Объем воды:  {water_volume} мл")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: [{solution_volume}] мл\n")
    file.write(f"Масса соли:  [{salt_mass:.2f}] г\n")
    file.write(f"Объем воды:  [{water_volume}] мл")

print("\nРецепт сохранён в файл recipe.txt")
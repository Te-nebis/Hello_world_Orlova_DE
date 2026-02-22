nutrient_name = input("Название питательной среды:")
nutrient_name_grade = nutrient_name.upper()
agar_concentration = input("Концентрация агара (%):")
sterilization_temperature = input("Tемпература стерилизации (°C):")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"Название питательной среды: {nutrient_name_grade}\n")
    file.write(f"Концентрация агара: {agar_concentration} %\n")
    file.write(f"Температура стерилизации: {sterilization_temperature}\n")

print("Файл 'recipe.txt' успешно сформирован")

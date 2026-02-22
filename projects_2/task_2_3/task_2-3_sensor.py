operator_name = input("Введите имя оператора:")
value_pressure = input("Введите текущее значение давления (Па):")
with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"{operator_name}\t {value_pressure}\n")
print("Данные успешно сохранены в sensor_log.txt")
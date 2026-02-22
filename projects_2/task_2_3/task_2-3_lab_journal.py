researcher_name = input("Введите ФИО исследователя:")
data = input("Введите дату:")
experiment = input("Введите название эксперимента:")
conclusion = input("Введите вывод:")
with open("journal.txt.", "w", encoding="utf-8" ) as file:
    file.write(f"+--------------------------------------------------+\n")
    file.write(f"| Электронный лабораторный журнал                  |\n")
    file.write(f"+--------------------------------------------------+\n")
    file.write(f"| ФИО исследователя : {researcher_name:<35} |\n")
    file.write(f"| Дата              : {data:<35}|\n")
    file.write(f"| Эксперимент       : {experiment:<35}\n")
    file.write(f"+--------------------------------------------------+\n")
    file.write(f"| Вывод:                                           |\n")
    file.write(f"|                                                  |\n")
    file.write(f"|                                                  |\n")
    file.write(f"|                                                  |\n")
    file.write(f"+--------------------------------------------------+")
print("Файл 'journal.txt.' успешно сформирован!")

    


reagent_name = input()
reagent_number = int(input())
print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_number} шт.")
file_path = "C:/Users/gusen/OneDrive/Документы/orlova_de/projects_2/task_2_2/inventory.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(f"Реактив {reagent_name} поступил на склад в количестве {reagent_number} шт.")

#!/bin/bash

# Проверяем, существует ли файл students.txt
if [ ! -f students.txt ]; then
    echo "Файл students.txt не найден!"
    exit 1
fi

echo "=== Статистика по оценкам студентов ==="

# Сумма всех оценок
sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "Сумма всех оценок: $sum"

# Средняя оценка
average=$(awk '{sum += $2} END {printf "%.2f", sum/NR}' students.txt)
echo "Средняя оценка: $average"

# Максимальная оценка
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END {print max}' students.txt)
echo "Максимальная оценка: $max"

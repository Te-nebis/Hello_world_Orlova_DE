#!/bin/bash
if [ ! -f data.csv ]; then
    echo "Файл data.csv не найден!"
    exit 1
fi

echo "=== Названия товаров ==="
cut -d',' -f2 data.csv

echo -e "\n=== Товары дороже 20 ==="
awk -F',' '$3 > 20 {print $2 " - " $3 " руб."}' data.csv

echo -e "\n=== Общая стоимость всех товаров ==="
total=$(awk -F',' '{sum += $3} END {print sum}' data.csv)
echo "Общая стоимость: $total руб."

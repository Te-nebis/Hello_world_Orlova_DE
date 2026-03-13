#!/bin/bash

echo "Калькулятор индекса массы тела (ИМТ)"

echo "Введите ваш вес (в килограммах):"
read weight

echo "Введите ваш рост (в метрах, например 1.75):"
read height

bmi=$(echo "$weight / ( $height * $height )" | bc)

rounded_bmi=$(echo "($bmi + 0.5) / 1" | bc)

echo "Ваш индекс массы тела: $rounded_bmi"

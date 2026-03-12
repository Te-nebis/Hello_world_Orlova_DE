bash
#!/bin/bash

echo "Калькулятор индекса массы тела (ИМТ)"

# Запрашиваем массу
echo "Введите ваш вес (в килограммах):"
read weight

# Запрашиваем рост
echo "Введите ваш рост (в метрах, например 1.75):"
read height

# Вычисляем ИМТ (bc — для дробных чисел)
bmi=$(echo "$weight / ( $height * $height )" | bc)

# Округляем до целого
rounded_bmi=$(echo "($bmi + 0.5) / 1" | bc)

echo "Ваш индекс массы тела: $rounded_bmi"

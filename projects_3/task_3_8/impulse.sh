#!/bin/bash

read -p "Введитеу массу (кг): " MASS
read -p "Введите рост (м): " HEIGHT

BMI=$((MASS/(HEIGHT**2)))

echo "Ваш индекс массы тела: $BMI"

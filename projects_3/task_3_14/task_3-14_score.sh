#!/bin/bash

echo "=== Студенты с оценкой ВЫШЕ 80 ==="
awk '$2 > 80 {print $1 " - " $2}' students.txt

echo -e "\n=== Студенты с оценкой НИЖЕ 70 ==="
awk '$2 < 70 {print $1 " - " $2}' students.txt

echo -e "\n=== ПЕРВАЯ строка файла ==="
head -n 1 students.txt

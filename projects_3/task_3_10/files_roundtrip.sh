#!/bin/bash

# Создаем 10 текстовых файлов
for i in {1..10}
do
    touch "test$i.txt"
done

echo "Файлы созданы: test1.txt, test2.txt, ..., test10.txt"

# Удаляем файлы в обратном порядке
i=10
while [ $i -ge 1 ]
do
    rm "test$i.txt"
    echo "Удален файл: test$i.txt"
    ((i--))
done

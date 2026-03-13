#!/bin/bash
#Создание 
for i in {1..10}
do
    touch "test$i.txt"
done

echo "Файлы созданы: test1.txt, test2.txt, ..., test10.txt"
№Удаление(тот же порядок)
i=10
while [ $i -ge 1 ]
do
    rm "test$i.txt"
    echo "Удален файл: test$i.txt"
    ((i--))
done

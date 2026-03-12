#!/bin/bash

# Заменяем пробелы на символы табуляции в файле sequences.txt
sed -i 's/ /\t/g' sequences.txt

#!/bin/bash

echo -e "Файл\tA\tT\tG\tC"

for file in *.fasta; do
    if [[ -s "$file" ]]; then
        # Убираем строки с '>', затем склеиваем последовательность
        seq=$(grep -v "^>" "$file" | tr -d '\n')
        
        A_count=$(echo "$seq" | grep -o "A" | wc -l)
        T_count=$(echo "$seq" | grep -o "T" | wc -l)
        G_count=$(echo "$seq" | grep -o "G" | wc -l)
        C_count=$(echo "$seq" | grep -o "C" | wc -l)

        echo -e "$file\t$A_count\t$T_count\t$G_count\t$C_count"
    fi
done

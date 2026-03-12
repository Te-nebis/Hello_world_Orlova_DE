#!/bin/bash

# Используем grep для поиска строки с текущим пользователем
grep "$USER" /etc/passwd

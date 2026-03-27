a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b:
    min = a
else:
    min = b

if c < min:
    min = c

if d < min:
    min = d

print(min) 
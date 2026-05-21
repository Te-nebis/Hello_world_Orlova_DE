import pandas as pd

df = pd.read_csv('wild_boars.csv')

print("Длина клыков всех кабанов:")
print(df['tusk_length_cm'])

print("Длина самых коротких и самых длинных клыков:")
print(df['tusk_length_cm'].max())
print(df['tusk_length_cm'].min())
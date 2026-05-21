import pandas as pd

df = pd.read_csv('wild_boars.csv')

grouped = df.groupby('gender')['tusk_length_cm']
cv_tusk = (grouped.std() / grouped.mean()) * 100

print("Коэффициент вариации по параметру длины клыков:")
print(f"Male CV: {cv_tusk['Male']:.1f} %")
print(f"Female CV: {cv_tusk['Female']:.1f} %")

cv_tusk.to_csv('tusk_length_cm.csv')


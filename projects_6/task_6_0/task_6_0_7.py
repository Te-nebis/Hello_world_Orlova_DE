import pandas as pd

df = pd.read_csv('wild_boars.csv')

columns = df[['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 
              'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']]

variance = columns.var()
std_dev = columns.std()
cv = (std_dev / columns.mean()) * 100


variance.to_csv('variance.csv')
std_dev.to_csv('std_deviation.csv')
cv.to_csv('cv.csv')

print("Дисперсия:")
print(variance)
print("Стандартное отклонение:")
print(std_dev)
print("Коэффициент вариации (%):")
print(cv)
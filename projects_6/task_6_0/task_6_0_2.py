import pandas as pd

df = pd.read_csv('wild_boars.csv')

columns = ['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 
           'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']

means = df[columns].mean()

print(means)


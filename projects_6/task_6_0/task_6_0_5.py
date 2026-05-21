import pandas as pd

df = pd.read_csv('wild_boars.csv')

columns = ['age_years', 'length_cm', 'shoulder_height_cm', 
           'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']

percentiles = df[columns].quantile([0.25, 0.50, 0.75, 0.90, 0.95, 1.00])

print(percentiles)
percentiles.to_csv('percentiles.csv')


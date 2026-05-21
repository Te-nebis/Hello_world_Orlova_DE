import pandas as pd

df = pd.read_csv('wild_boars.csv')

medians = df[['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 
                      'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']].median()
print(medians)
medians.to_csv('medians.csv')
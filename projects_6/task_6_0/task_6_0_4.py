import pandas as pd

df = pd.read_csv("wild_boars.csv")

mode = df[['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 
           'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']].mode()

print(mode)                    
mode.to_csv('mode.csv')        
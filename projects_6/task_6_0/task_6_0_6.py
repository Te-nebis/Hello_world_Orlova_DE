import pandas as pd
df = pd.read_csv('wild_boars.csv')

# Считаем Q1 и Q3 для каждого пола
q1 = df.groupby('gender')['length_cm'].quantile(0.25)
q3 = df.groupby('gender')['length_cm'].quantile(0.75)


iqr = q3 - q1

print("Межквартильный размах по длине тела:")
print(f"Male IQR: {iqr['Male']:.1f} cm")
print(f"Female IQR: {iqr['Female']:.1f} cm")

iqr.to_csv('iqr_length.csv')





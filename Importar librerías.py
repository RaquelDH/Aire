import pandas as pd

# Lee el archivo CSV en un DataFrame
df = pd.read_csv('Calidad_del_aire.csv')

# Muestra las primeras filas (por defecto, muestra las primeras 5 filas)
print(df.head())
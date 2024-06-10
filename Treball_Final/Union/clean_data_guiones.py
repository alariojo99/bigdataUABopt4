import pandas as pd

def clean_data(filepath):
    # Leer el archivo CSV
    df = pd.read_csv(filepath)

    # Lista de columnas a procesar para cambiar "-" por 0
    columns_to_zero = ['Appearances', 'Points per match', 'Goals', 'Assists', 'Own goals',
                       'Subtitutions on', 'Subtitutions off', 'Yellow cards',
                       'Second yellow cards', 'Red cards', 'Penalty goals',
                       'Minutes per goal', 'Minutes played']

    # Reemplazar "-" por 0 en las columnas especificadas
    for column in columns_to_zero:
        df[column] = df[column].replace('-', 0)


    # Guardar el DataFrame modificado en un nuevo archivo CSV
    df.to_csv('cleaned_data.csv', index=False)

# Ruta al archivo CSV original
filepath = 'tots_jugadors_total.csv'
clean_data(filepath)

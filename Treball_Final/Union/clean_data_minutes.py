import pandas as pd

def clean_data(filepath):
    # Leer el archivo CSV
    df = pd.read_csv(filepath)

    # Lista de columnas a procesar para cambiar "-" por 0
    columns_to_zero = ['Minutes per goal', 'Minutes played']

    df['Minutes per goal'] = df['Minutes per goal'].str.replace("'", "")
    df['Minutes played'] = df['Minutes played'].str.replace("'", "")

    # Guardar el DataFrame modificado en un nuevo archivo CSV
    df.to_csv('very_cleaned_data.csv', index=False)

# Ruta al archivo CSV original
filepath = 'cleaned_data.csv'
clean_data(filepath)

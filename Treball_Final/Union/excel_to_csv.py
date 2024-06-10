import os
import pandas as pd

def convert_xlsx_to_csv(directory):
    # Recorrer todos los archivos en el directorio especificado
    for filename in os.listdir(directory):
        if filename.endswith('.xlsx'):
            print(f"Procesando archivo: {filename}")
            # Construir el path completo al archivo
            filepath = os.path.join(directory, filename)
            # Cargar el archivo Excel
            df = pd.read_excel(filepath)
            # Construir el nombre del nuevo archivo CSV
            csv_filename = filename.replace('.xlsx', '.csv')
            csv_filepath = os.path.join(directory, csv_filename)
            # Guardar DataFrame como CSV
            df.to_csv(csv_filepath, index=False)
            print(f"Archivo convertido y guardado como: {csv_filename}")

# Ruta al directorio donde están los archivos Excel
directory_path = '.'
# Llamar a la función
convert_xlsx_to_csv(directory_path)

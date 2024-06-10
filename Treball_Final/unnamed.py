import os
import pandas as pd

def count_files_with_unnamed_columns(directory):
    count = 0
    # Recorrer todos los archivos en el directorio especificado
    for filename in os.listdir(directory):
        if filename.endswith('.xlsx'):
            print(filename)
            # Construir el path completo al archivo
            filepath = os.path.join(directory, filename)
            try:
                # Cargar el archivo Excel
                df = pd.read_excel(filepath)
                # Comprobar si alguna columna contiene 'Unnamed'
                if any('Unnamed' in col for col in df.columns):
                    count += 1
            except Exception as e:
                print(f"No se pudo procesar el archivo {filename}: {e}")
    return count

# Ruta al directorio donde están los archivos Excel
directory_path = '.'
# Llamar a la función y mostrar el resultado
unnamed_count = count_files_with_unnamed_columns(directory_path)
print(f"Número de archivos con columnas 'Unnamed': {unnamed_count}")

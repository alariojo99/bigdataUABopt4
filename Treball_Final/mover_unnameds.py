import os
import pandas as pd
import shutil

def count_and_move_files_with_unnamed_columns(directory):
    count = 0
    # Asegurarse de que la carpeta "archivos_unnamed" existe
    unnamed_dir = os.path.join(directory, 'archivos_unnamed')
    if not os.path.exists(unnamed_dir):
        os.makedirs(unnamed_dir)

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
                    # Mover archivo a la carpeta "archivos_unnamed"
                    shutil.move(filepath, os.path.join(unnamed_dir, filename))
            except Exception as e:
                print(f"No se pudo procesar el archivo {filename}: {e}")
    return count

# Ruta al directorio donde están los archivos Excel
directory_path = '.'
# Llamar a la función y mostrar el resultado
unnamed_count = count_and_move_files_with_unnamed_columns(directory_path)
print(f"Número de archivos con columnas 'Unnamed' movidos a 'archivos_unnamed': {unnamed_count}")

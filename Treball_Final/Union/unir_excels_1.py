import pandas as pd
import os

def unir_excel_desde_carpeta(nombre_arxiu_sortida):
    # Obtindre la llista d'arxius en el directori actual
    arxius_en_carpeta = os.listdir()

    # Filtrar els arxius que acaben en .xlsx
    arxius_excel = [arxiu for arxiu in arxius_en_carpeta if arxiu.endswith('jugadors.csv')]

    # Crear una llista per emmagatzemar els DataFrames de cada arxiu Excel
    llista_dfs = []

    # Iterar sobre cada arxiu Excel
    for arxiu in arxius_excel:
        # Llegir l'arxiu Excel i afegir el DataFrame a la llista
        df = pd.read_csv(arxiu)
        llista_dfs.append(df)

    # Concatenar tots els DataFrames en un sol
    df_final = pd.concat(llista_dfs)

    # Guardar el DataFrame final en un nou arxiu Excel
    df_final.to_csv(nombre_arxiu_sortida, index=False)

    print(f"Els arxius Excel a la carpeta s'han unit correctament en '{nombre_arxiu_sortida}'.")

# Utilització de la funció
nombre_arxiu_sortida = "tots_jugadors_total.csv"  # Nom de l'arxiu Excel de sortida
unir_excel_desde_carpeta(nombre_arxiu_sortida)
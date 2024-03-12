import pandas as pd

"""Objetivo: Crea un documento .CSV con 5 columnas:

Columna 1: Nombre y apellidos (en una única cadena de texto) de cada alumno
Columna 2: Nota de cada alumno
Columna 3: Nota "en texto" para cada alumno:
    Si la nota final es inferior a 5, añadir el texto "suspendido".
    Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".
    Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".
    Si la nota es igual o superior a 7, añadir el texto "notable".
    Si la nota supera el 9, añadir el texto "Excelente".
    Si la nota equivale a un 10, añadir el texto "matrícula de honor".
Columna 4: Diferencia de nota respecto a la mediana del grupo
Columna 5: Diferencia de nota (expreseda en porcentaje) respecto a la mediana del grupo
Condiciones especiales
Antes de hacer los cálculos, debes sumar UN punto a cada alumno, pero la nota máxima nunca puede superar el 10."""

notes = [1,6,8,9,10,6,5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]

df = pd.DataFrame()

full_names = []

for i in range(len(alumnes)):
    full_name = f'{alumnes[i]} {cognoms[i]}'
    full_names.append(full_name)

new_notes = []

for nota in notes:
    if nota < 10:
        new_nota = nota + 1
        new_notes.append(new_nota)
    else:
        new_notes.append(nota)

notes_textuals = []

for nota in new_notes:
    if nota < 5:
        notes_textuals.append("Suspendido")
    elif 5 >= nota < 6:
        notes_textuals.append("Aprobado")
    elif 6 >= nota < 7:
        notes_textuals.append("Bien")
    elif 7 >= nota < 9:
        notes_textuals.append("Notable")
    elif 9 >= nota < 10:
        notes_textuals.append("Excelente")
    elif nota == 10:
        notes_textuals.append("Matricula de honor")

dades = []

for nom, nota, nota_texto in zip (full_names, new_notes, notes_textuals):
    alumno = {
        "Nombre": nom,
        "Nota": nota,
        "Calificación": nota_texto
    }
    dades.append(alumno)

df = pd.DataFrame(dades)

df.to_csv("dades.csv", index= False)
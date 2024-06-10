import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os
import re

def extraer_y_juntar(numero_jugador, random_number):

    for jugador in numero_jugador:
        try:
            if not numero_jugador:  # Verificar si la lista está vacía
                print("La lista de números de jugador está vacía.")
                break

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
            }

            resposta = requests.get(
                f"https://www.transfermarkt.com/lionel-messi/leistungsdatendetails/spieler/{jugador}/saison//verein/0/liga/0/wettbewerb//pos/0/trainer_id/0/plus/1",
                headers=headers,
            )

            resposta.raise_for_status()  # Lanzar excepción en caso de error HTTP

            soup = BeautifulSoup(resposta.text, "html.parser")
            final = soup.find("div", id="yw1")
            tabla = final.find_next("table")

            nom = soup.find("h1", class_="data-header__headline-wrapper").text
            nom = re.sub(r'[^a-zA-Z\s]', '', nom).strip()

            df = pd.read_html(tabla.prettify())[0]

            # Agregar columna de nombre del jugador
            df["name"] = nom

            #Afegir la columna ID
            df["id_jugador"] = jugador


            # Agregar columna de posición
            posicion = soup.find_all("li", class_="data-header__label")
            pos = posicion[4]
            a = pos.find_all("span")
            position_text = ""
            for span in a:
                position_text += span.text.strip() + " "
            df["position_text"] = position_text.strip()


            df.to_excel(f"player_{jugador}.xlsx", index=False)
            time.sleep(random_number)
            print(f"Todo bien en {jugador}")

            # Leer el archivo excel recién creado y renombrar las columnas
            df = pd.read_excel(f"player_{jugador}.xlsx")
            df.columns.values[0] = "Season"
            df.columns.values[2] = "Competitició"
            df.columns.values[3] = "Club"
            df.columns.values[4] = "Squad"
            df.columns.values[5] = "Appearances"
            df.columns.values[6] = "Points per match"
            df.columns.values[7] = "Goals"
            df.columns.values[8] = "Assists"
            df.columns.values[9] = "Own goals"
            df.columns.values[10] = "Subtitutions on"
            df.columns.values[11] = "Subtitutions off"
            df.columns.values[12] = "Yellow cards"
            df.columns.values[13] = "Second yellow cards"
            df.columns.values[14] = "Red cards"
            df.columns.values[15] = "Penalty goals"
            df.columns.values[16] = "Minutes per goal"
            df.columns.values[17] = "Minutes played"

            df = df.drop("Competition", axis=1)
            df = df.drop("Unnamed: 18", axis=1)

            imagenes = soup.find_all("img", class_="tiny_wappen")

            list_club_names = []

            for img in imagenes:
                club_name = img.get("alt")
                list_club_names.append(club_name)

            df2 = pd.DataFrame(list_club_names)
            df["clubs_ok"] = df2[0]
            df = df.iloc[:-1]  # Eliminar la última fila

            # Guardar el DataFrame final en un nuevo archivo Excel
            df.to_excel(f"player_{jugador}.xlsx", index=False)

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP para el jugador {jugador}: {e}")
            # Obtener el último jugador procesado con éxito
            ultimo_jugador = jugador - 1 if jugador != numero_jugador[0] else numero_jugador[0]
            print(f"Reanudando desde el último jugador exitoso ({ultimo_jugador})...")
            break
        except IndexError:
            print(f"Error: No se pudo encontrar la tabla de datos para el jugador {jugador}.")

            continue
        except Exception as e:
            print(f"Error inesperado para el jugador {jugador}: {e}")



# Utilización de la función
numero_jugador = range(99922, 100000, 1)
random_number = random.randint(1, 3)
extraer_y_juntar(numero_jugador, random_number)







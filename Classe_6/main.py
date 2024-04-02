### Llibreries a instal·lar #################
# pip install beautifulsoup4                #
# pip install requests                      #
# pip install spotipy                       #
# pip install lxml                          #
# pip install openpyxl                      #
#############################################

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import glob
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = "2d24e72bccfc459d8c6eb1408f954097"
SPOTIPY_CLIENT_SECRET = "29126da8bfd742a39389cb3a03766b64"

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

rango = range(2000,2024,1)

def extract_wiki(rango):
    for r in rango:
        try:
            resposta = requests.get(f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{r}")
            codi_web = resposta.text

            soup = BeautifulSoup(codi_web, "html.parser")
            final = soup.find('span', id="Final")
            tabla = final.find_next("table")
            df = pd.read_html(str(tabla))[0]

            df.to_excel(f"final-{r}.xlsx", index=False)
            time.sleep(1)
            #print(df)
            print(f"Todo bien en {r}")
        except AttributeError:
            print(f"Problema en {r}")

#extract_wiki(rango)

def juntar():
    files = glob.glob("*.xlsx")

    list_of_dfs = []

    for f in files:
        df = pd.read_excel(f)
        any = f.split("-")[1].split(".")[0]
        df["año"] = any
        df.columns.values[2] = "Cantante"
        df.columns.values[5] = "Puntos"
        df.columns.values[0] = "N."

        list_of_dfs.append(df)

    final_df = pd.concat(list_of_dfs)
    final_df.to_excel("final.xlsx", index=False)

#juntar()

df = pd.read_excel("final.xlsx")
#print(df)

for index,row in df.iterrows():
    cantant = row["Cantante"]
    song = row["Canción"]
    q = f"{song}%track%{cantant}%artist%"
    resposta = sp.search(q, limit=1, offset=0, type="track", market=None)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)
    time.sleep(15)


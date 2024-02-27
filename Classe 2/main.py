import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

api_client_id = "2d24e72bccfc459d8c6eb1408f954097"
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

artist_id = "7ltDVBr6mKbRvohxheJ9h1"
related = spotify.artist_related_artists(artist_id)

artistes = related["artists"]

llista_artistes = []
i = 0

for a in artistes:
    i = i+1
    name = a["name"]
    followers = a["followers"]["total"]
    link = a["external_urls"]["spotify"]
    id = a["id"]
    #print(name, followers, link)

    frame = pd.DataFrame({
        "semilla": artist_id,
        "name": name,
        "followers": followers,
        "link": link,
        "id": id,
    }, index=[i])
    llista_artistes.append(frame)

    related_2 = spotify.artist_related_artists(id)
    artistes_2 = related_2["artists"]

    for a_2 in artistes_2:
        i = i + 1
        name = a_2["name"]
        followers = a_2["followers"]["total"]
        link = a_2["external_urls"]["spotify"]
        id_2 = a_2["id"]
        # print(name, followers, link)

        frame = pd.DataFrame({
            "semilla": id,
            "name": name,
            "followers": followers,
            "link": link,
            "id": id_2,
        }, index=[i])
        llista_artistes.append(frame)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(related, f, indent=4)

final = pd.concat(llista_artistes)

print(final)

final.to_excel("dataset.xlsx")

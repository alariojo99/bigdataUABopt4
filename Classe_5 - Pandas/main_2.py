import pandas as pd

df = pd.read_excel("dataset.xlsx")

#df["Average views"] = df["viewCount"].mean()
df["Desviación Absoluta Views"] = df["viewCount"] - df["viewCount"].mean()
df["Desviación Absoluta Likes"] =  df["likeCount"] - df["likeCount"].mean()
df["Desviación Absoluta Comments"] = df["commentCount"] - df["commentCount"].mean()

df["Desviación Porcentual Views"] = round(((df["viewCount"] - df["viewCount"].mean())/df["viewCount"].mean())*100,2)
df["Desviación Porcentual Likes"] = round(((df["likeCount"] - df["likeCount"].mean())/df["likeCount"].mean())*100,2)
df["Desviación Porcentual Comments"] = round(((df["commentCount"] - df["commentCount"].mean())/df["commentCount"].mean())*100,2)

df = df.drop(["channelId", "categoryId", "channelTitle", "tags", "publishedAt", "blocked_at"], axis=1)

indice_max_views = df['viewCount'].idxmax()
most_views_video = df.loc[indice_max_views, 'title']

indice_max_likes = df['likeCount'].idxmax()
most_likes_video = df.loc[indice_max_likes, 'title']

indice_max_comments = df['commentCount'].idxmax()
most_comments_video = df.loc[indice_max_comments, 'title']

print(most_views_video, most_comments_video, most_likes_video)


df.to_excel("new_dataset.xlsx")
import requests
import csv
from datetime import datetime


CLIENT_ID = '6vnwxwyuvhokk2caqxbm6x9rihglat'
CLIENT_SECRET = 'yqfqfh9ri2bxmo8nzj0hcsnvgk08p6'


def get_access_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    return response.json()['access_token']


access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)


def get_games():
    url = 'https://api.igdb.com/v4/games'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    query = """
        fields name, summary, first_release_date, genres.name, platforms.name;
        sort rating desc;
        where rating != null & first_release_date != null;
        limit 20;
    """
    
    response = requests.post(url, headers=headers, data=query)
    
    if response.status_code != 200:
        print("Erreur API :", response.json())
        return []
    
    return response.json()

def format_date(timestamp):
    if timestamp:
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
    return "N/A"


def truncate_summary(summary, length=200):
    if summary and len(summary) > length:
        return summary[:length] + "..."
    return summary


def save_to_csv(games):
    with open('games.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(["Nom", "Résumé", "Date de sortie", "Genres", "Plateformes"])
        
        for game in games:
            name = game.get("name", "N/A")
            summary = truncate_summary(game.get("summary", "N/A"))
            release_date = format_date(game.get("first_release_date"))
            
            genres = ", ".join([genre["name"] for genre in game.get("genres", [])])
            platforms = ", ".join([platform["name"] for platform in game.get("platforms", [])])
            
            writer.writerow([name, summary, release_date, genres, platforms])

    print("✅ Fichier 'games.csv' enregistré avec succès !")


games_data = get_games()
save_to_csv(games_data)

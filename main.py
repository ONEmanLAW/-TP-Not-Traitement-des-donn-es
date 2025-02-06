import requests
import psycopg2


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

def get_game_data(game_name):
    url = 'https://api.igdb.com/v4/games'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    query = f'fields name,genres,platforms,summary; search "{game_name}";'
    response = requests.post(url, headers=headers, data=query)
    return response.json()

game_data = get_game_data("The Witcher 3")
print(game_data)

'''import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8b11b5ad360b2762d6a4ff06696ebba3'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}
body_pokemon = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)
print(response.text)'''


'''import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8b11b5ad360b2762d6a4ff06696ebba3'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}
body_new_name_pokemon = {
    "pokemon_id": "123531",
    "name": "Резеда",
    "photo_id": 1
}

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name_pokemon)
print(response.text)'''

'''import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8b11b5ad360b2762d6a4ff06696ebba3'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}
body_add_pokeball = {
    "pokemon_id": "123531"
}

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response.text)'''
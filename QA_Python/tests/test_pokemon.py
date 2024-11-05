import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8b11b5ad360b2762d6a4ff06696ebba3'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}
TRAINER_ID = '6980'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_trainer_id():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == "6980"

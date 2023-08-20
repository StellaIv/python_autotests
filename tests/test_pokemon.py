import requests
import pytest

token = 'c79e83f818cf8d4ab62c8d4066dcc4ed'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1856})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1856})
    assert response.json()['trainer_name'] == '321'

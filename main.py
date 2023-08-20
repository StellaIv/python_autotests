import requests

token = 'c79e83f818cf8d4ab62c8d4066dcc4ed'
host = 'https://api.pokemonbattle.me:9104'

response_generate_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
    }, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})
print(response_generate_pokemon.text)

response_change_name_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6323",
    "name": "Poke",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
    }, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})
print(response_change_name_pokemon.text)

response_add_pokemon = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6323"
    }, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})
print(response_add_pokemon.text)


#API pokemonbattle
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6c7955443f7d64acf1fffd0d4150e3dd'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {    
    "name": "generate",
    "photo_id": -1
}

#Create a Pokemon
response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']
print(pokemon_id)

#Change a Pokemon's name
body_change = {
    "pokemon_id": pokemon_id,
    "name": "Patrick",
    "photo_id": -1
}
response_create = requests.put(url= f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_create.text)

#Catch a Pokemon in a Pokeball
body_pokeboll = {
    "pokemon_id": pokemon_id
}
response_create = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_create.text)



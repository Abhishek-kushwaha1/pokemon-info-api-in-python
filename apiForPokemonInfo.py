import requests

api_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{api_url}/pokemon/{name}"
    respons = requests.get(url)
    if respons.status_code == 200:
        print("Data retrive success !")
        return respons.json()
    else:
        print (f"Failed to retrive data {respons.status_code}")


# pokemon_name = "pikachu"
pokemon_name = input("Enter the name of a pokemone : ")
pokemon_info = get_pokemon_info(pokemon_name.lower())
if pokemon_info:
    print(f"Name of the pokemone is : {pokemon_info["name"].capitalize()}")
    print(f"Height of the {pokemon_info["name"]} is : {pokemon_info["height"]} Units")


import requests

# Funktion zum Abrufen der deutschen Namen
def fetch_german_name(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        names = data.get('names', [])
        german_name = next((name['name'] for name in names if name['language']['name'] == 'de'), None)
        return german_name
    else:
        print(f"Fehler beim Abrufen von Pokémon-Spezies {pokemon_id}")
        return None

# Test: Abrufen der Namen für die ersten 10 Pokémon
for pokemon_id in range(1, 11):
    german_name = fetch_german_name(pokemon_id)
    if german_name:
        print(f"Pokémon {pokemon_id}: {german_name}")
    else:
        print(f"Kein deutscher Name für Pokémon {pokemon_id} gefunden.")

import requests
import psycopg2


# PostgreSQL-Verbindung
conn = psycopg2.connect(
    dbname="RandomMonGenerator", 
    user="postgres", 
    password="postgres", 
    host="localhost", 
    port="5432"
)

# Cursor erstellen
cursor = conn.cursor()

# Mapping von englischen zu deutschen Typen
type_mapping = {
    "normal": "Normal",
    "fire": "Feuer",
    "water": "Wasser",
    "grass": "Pflanze",
    "electric": "Elektro",
    "ice": "Eis",
    "fighting": "Kampf",
    "poison": "Gift",
    "ground": "Boden",
    "flying": "Flug",
    "psychic": "Psycho",
    "bug": "Käfer",
    "rock": "Gestein",
    "ghost": "Geist",
    "dragon": "Drache",
    "dark": "Unlicht",
    "steel": "Stahl",
    "fairy": "Fee"
}

# Funktion zum Abrufen des deutschen Pokémon-Namens
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

# Funktion zum Abrufen von Pokémon-Daten inkl. Typen
def fetch_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        german_name = fetch_german_name(pokemon_id)
        if not german_name:
            return None
        
        types = [t['type']['name'] for t in data['types']]
        type1 = type_mapping.get(types[0], types[0].capitalize())
        type2 = type_mapping.get(types[1], types[1].capitalize()) if len(types) > 1 else ''
        dexnumber = data['id']

        # Bestimmen der Generation
        if dexnumber <= 151:
            generation = 1
        elif dexnumber <= 251:
            generation = 2
        elif dexnumber <= 386:
            generation = 3
        elif dexnumber <= 493:
            generation = 4
        elif dexnumber <= 649:
            generation = 5
        elif dexnumber <= 721:
            generation = 6
        elif dexnumber <= 809:
            generation = 7
        elif dexnumber <= 898:
            generation = 8
        else:
            generation = 9

        return [pokemon_id, german_name, type1, type2, generation, dexnumber]
    else:
        print(f"Fehler beim Abrufen von Pokémon {pokemon_id}")
        return None

# Einfügen der Pokémon-Daten in die Datenbank
def insert_pokemon_data(pokemon_data):
    insert_query = '''
    INSERT INTO pokemon (name, type1, type2, generation, dexnumber)
    VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (
        pokemon_data["name"],
        pokemon_data["type1"],
        pokemon_data["type2"],
        pokemon_data["generation"],
        pokemon_data["dexnumber"]
    ))
    conn.commit()

# Abrufen und Einfügen der Daten für die ersten 1025 Pokémon
for pokemon_id in range(1, 1026):
    print(f"Lade Pokémon {pokemon_id}...")
    pokemon_data = fetch_pokemon_data(pokemon_id)
    if pokemon_data:
        insert_pokemon_data(pokemon_data)

# Verbindung schließen
cursor.close()
conn.close()

print("Alle Pokémon-Daten wurden erfolgreich eingefügt!")

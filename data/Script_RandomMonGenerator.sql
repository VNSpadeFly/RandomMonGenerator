--Script fürs Erstellen der Datenbank für den RandomMonGenerator
--Eigene Database erstellen
CREATE DATABASE RandomMonGenerator;

--Table erstellen mit Fakten zu Pokemon
CREATE TABLE public.pokemon (
    id SERIAL PRIMARY KEY, --key, nicht zu verwechseln mit NationalDex
    name TEXT NOT NULL, --Name des Pokemons
    type1 TEXT NOT NULL, --Typ des Pokemon
    type2 TEXT, --Secondary Type, kann auch NULl sein
    generation INTEGER NOT NULL, --generation in der es offiziell erschienen ist. Mainline Games
    sprite BYTEA, -- Für die Binärdaten der Pokémon-Bilder
    dexnumber Integer NOT NULL --Nummer im NationalDex
);

--Table mit Routen und Citys?

--Copy von Daten über eine CSV
COPY pokemon (id, name, type1, type2, generation, dexnumber) 
FROM 'C:\Users\vly\OneDrive - it-novum GmbH\Dokumente\Dokumente Viet Hung Ly\Privat\RandomMonGenerator\RandomMonGenerator\Pokemon_data.csv 
DELIMITER ',' 
CSV HEADER;



import psycopg

# Verbindung zur Datenbank herstellen
def connect_to_db():
    conn = psycopg.connect(
        host="localhost",          # Dein Host
        dbname="RandomMonGenerator", # Dein Datenbankname
        user="dein_user",          # Dein Benutzername
        password="dein_passwort",  # Dein Passwort
        port=5432                  # Standard PostgreSQL-Port
    )
    return conn

# Teste die Verbindung
if __name__ == "__main__":
    try:
        conn = connect_to_db()
        print("Verbindung zur Datenbank erfolgreich!")
        conn.close()
    except Exception as e:
        print(f"Fehler bei der Verbindung: {e}")

import sqlite3

conn = sqlite3.connect("brukere.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS brukere (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    navn TEXT NOT NULL,
    pc_nummer TEXT NOT NULL
    problem TEXT
)
''')
conn.commit()

def legg_til_bruker():
    navn = input("Skriv inn navn: ").strip()
    pc_nummer = input("Skriv inn PC-nummer: ").strip()
    problem = input("Beskriv inn problemet: ").strip()

    if not navn or not pc_nummer:
        print("Navn og pc-nummer kan ikke være tomme.")
        return

    cursor.execute("INSERT INTO brukere (navn, pc_nummer, problem) VALUES (?,?,?)", (navn, pc_nummer, problem))
    conn.commit()
    print("Bruker lagt til!")

def vis_brukere():
    cursor.execute("SELECT * FROM brukere")
    brukere = cursor.fetchall()
    if not brukere:
        print("Ingen brukere registrert.")
    else: 
        for rad in brukere:
            print(f"ID: {rad[0]}, Navn: {rad[1]}, PC-nummer: {rad[2]}, Problem: {rad[3]}")

def meny():
    while True:
        print("\n1. Legg til bruker\n2. Vis alle brukere\n3. Avslutt")
        valg = input("Velg et alternativ: ").strip()
        if valg == "1":
            legg_til_bruker()
        elif valg == "2":
            vis_brukere()
        elif valg == "3":
            break
        else: 
            print("Ugyldig valg, prøv igjen.")

meny()
conn.close()

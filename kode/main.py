import sqlite3

conn = sqlite3.connect("brukere.db")
cursor = conn.cursor()

# Oppretter tabellen med nytt 'problem'-felt
cursor.execute('''
CREATE TABLE IF NOT EXISTS brukere (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    navn TEXT NOT NULL,
    pc_nummer TEXT NOT NULL,
    problem TEXT NOT NULL
)
''')
conn.commit()

def legg_til_bruker():
    navn = input("Skriv inn navn: ").strip()
    pc_nummer = input("Skriv inn PC-nummer: ").strip()
    problem = input("Beskriv problemet: ").strip()
    if navn and pc_nummer and problem:
        cursor.execute("INSERT INTO brukere (navn, pc_nummer, problem) VALUES (?, ?, ?)", (navn, pc_nummer, problem))
        conn.commit()
        print("Bruker lagt til!")
    else:
        print("Alle felt må fylles ut.")

def vis_brukere():
    cursor.execute("SELECT * FROM brukere")
    for rad in cursor.fetchall():
        print(f"ID: {rad[0]}, Navn: {rad[1]}, PC-nummer: {rad[2]}, Problem: {rad[3]}")

def meny():
    while True:
        print("\n1. Legg til bruker\n2. Vis alle brukere\n3. Avslutt")
        valg = input("Velg et alternativ: ")
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

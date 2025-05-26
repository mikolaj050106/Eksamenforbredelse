import sqlite3

conn = sqlite3.connect("brukere.db")
cursor = conn.cursor()

cursor.excecute('''
CREATE TABLE IF NOT EXISTS brukere (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    navn TEXT NOT NULL,
    pc_nummer TEXT NOT NULL
)
''')
conn.commit()

def legg_til_bruker():
    navn = input("Skriv inn navn")
    pc_nummer = input("skriv inn PC-nummer")
    cursor.excecute("INSERT INTO brukere (navn, pc_nummer) VALUES (?,?)", (navn, pc_nummer))
    conn.commit()
    print("Bruker lagt til!")

def vis_brukere():
    cursor.execute("SELECT * FROM brukere")
    for rad in cursor.fetchall():
        print(f"ID: {rad[0]}, Navn: {rad[1]}, PC-nummer: {rad[2]}")

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

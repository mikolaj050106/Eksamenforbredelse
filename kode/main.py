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
    con.commit()
    print("Bruker lagt til!")

def vis_brukere():
    cursor.execute("SELECT * FROM brukere")
    for rad in cursor.fetchall():
        print(f"ID: {rad[0]}, Navn: {rad[1]}, PC-nummer: {rad[2]}")


from flask import Flask, request, render_template_string 
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("brukere.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS brukere (navn TEXT, pcnummer TEXT)")

    if request.method == "POST":
        navn = request.form["navn"]
        pcnummer = request.form["pcnummer"]
        cursor.execute("INSERT INTO brukere (navn, pcnummer) VALUES (?, ?)", (navn, pcnummer))
        conn.commit()

    cursor.execute("SELECT navn, pcnummer FROM brukere")
    brukere = cursor.fetchall()
    print(brukere)  # For debugging
    conn.close()

    return render_template_string('''
    <h2>Registrer bruker</h2>
    <form method="POST">
        Navn: <input type="text" name="navn"><br>
        PC-nummer: <input type="text" name="pcnummer"><br>
        <input type="submit" value="Registrer">
    </form>
    <h3>Registrerte brukere:</h3>
    <ul>
        {% for navn, pcnummer in brukere %}
            <li>{{ navn }} – {{ pcnummer }}</li>
        {% endfor %}
    </ul>
    ''', brukere=brukere)

if __name__ == "__main__":
    app.run(debug=True)
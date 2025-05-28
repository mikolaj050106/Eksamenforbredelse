from flask import Flask, request, render_template_string 
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("brukere.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS brukere (navn TEXT, pcnummer TEXT, problem TEXT)")

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
    <html>
    <head>
        <title>Brukerregistrering</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                padding: 20px;
            }
            h2, h3 {
                color: #333;
            }
            form {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-width: 400px;
                margin-bottom: 30px;
            }
            input[type="text"] {
                width: 100%;
                padding: 8px;
                margin: 8px 0;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                background-color: #fff;
                margin: 5px 0;
                padding: 10px;
                border-radius: 4px;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.05);
            }
        </style>
    </head>
    <body>
        <h2>Registrer bruker</h2>
        <form method="POST">
            Navn: <input type="text" name="navn" required><br>
            PC-nummer: <input type="text" name="pcnummer" required><br>
            <input type="submit" value="Registrer">
        </form>
        <h3>Registrerte brukere:</h3>
        <ul>
            {% for navn, pcnummer in brukere %}
                <li><strong>{{ navn }}</strong> – {{ pcnummer }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    ''', brukere=brukere)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
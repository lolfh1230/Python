
from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Vytvoření databáze
DB_NAME = "finance.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category TEXT,
                amount REAL,
                type TEXT,
                date TEXT,
                description TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')

# Registrace nového uživatele
def register_user(username, password):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return False
    return True

# Přihlášení uživatele
def login_user(username, password):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        return user

# Přidání transakce
def add_transaction(user_id, category, amount, t_type, date, description):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (user_id, category, amount, type, date, description) VALUES (?, ?, ?, ?, ?, ?)",
                       (user_id, category, amount, t_type, date, description))
        conn.commit()

# Načtení transakcí
def get_transactions(user_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE user_id=?", (user_id,))
        return cursor.fetchall()

# Hlavní stránka s přihlášením
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login_user(username, password)
        if user:
            return redirect(url_for('dashboard', user_id=user[0]))
        else:
            return "Neplatné přihlašovací údaje."
    
    return render_template_string('''
        <h2>Přihlášení</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Uživatelské jméno" required><br>
            <input type="password" name="password" placeholder="Heslo" required><br>
            <input type="submit" value="Přihlásit se">
        </form>
        <a href="/register">Registrovat se</a>
    ''')

# Stránka pro registraci
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register_user(username, password):
            return redirect(url_for('login'))
        else:
            return "Uživatel už existuje."
    
    return render_template_string('''
        <h2>Registrace</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Uživatelské jméno" required><br>
            <input type="password" name="password" placeholder="Heslo" required><br>
            <input type="submit" value="Registrovat se">
        </form>
        <a href="/">Přihlásit se</a>
    ''')

# Hlavní stránka uživatele (dashboard)
@app.route('/dashboard/<int:user_id>', methods=['GET', 'POST'])
def dashboard(user_id):
    if request.method == 'POST':
        category = request.form['category']
        amount = request.form['amount']
        t_type = request.form['type']
        date = request.form['date']
        description = request.form['description']
        add_transaction(user_id, category, amount, t_type, date, description)
    
    transactions = get_transactions(user_id)
    return render_template_string('''
        <h2>Správa financí</h2>
        <form method="POST">
            Kategorie: <input type="text" name="category" required><br>
            Částka: <input type="number" name="amount" required><br>
            Typ: <select name="type">
                <option value="příjem">Příjem</option>
                <option value="výdaj">Výdaj</option>
            </select><br>
            Datum: <input type="date" name="date" required><br>
            Popis: <input type="text" name="description"><br>
            <input type="submit" value="Přidat transakci">
        </form>

        <h3>Seznam transakcí:</h3>
        <ul>
            {% for t in transactions %}
            <li>{{ t[3] }} - {{ t[2] }} Kč ({{ t[4] }}) - {{ t[6] }} - {{ t[5] }}</li>
            {% endfor %}
        </ul>
        <a href="/">Odhlásit se</a>
    ''', transactions=transactions)

if __name__ == '__main__':
    if not os.path.exists(DB_NAME):
        init_db()
    app.run(debug=True)

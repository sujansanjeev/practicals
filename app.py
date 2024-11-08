from flask import Flask
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM my_table")
    rows = cur.fetchall()
    conn.close()
    return {"data": [dict(row) for row in rows]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

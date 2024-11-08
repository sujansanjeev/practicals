from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# MySQL configurations from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'db')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'root')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'mydb')

mysql = MySQL(app)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Flask-MySQL App,hi"})

@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    users = cur.fetchall()
    cur.close()
    
    users_list = []
    for user in users:
        users_list.append({
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'created_at': str(user[3])
        })
    
    return jsonify(users_list)

@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.json
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO users (name, email) VALUES (%s, %s)''',
                (user_data['name'], user_data['email']))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from flask import Flask, request, redirect, url_for, session, Response, render_template
import os, dotenv
import mysql.connector
from datetime import date
import os
from dotenv import load_dotenv

dotenv.load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv('DB_host'),
    port=int(os.getenv('DB_PORT', 3306)),
    user=os.getenv('DB_username'),
    password=os.getenv('DB_password'),
    database=os.getenv('DB_name')
)
cursor = connection.cursor()

app = Flask(__name__)
app.secret_key = os.getenv('secret_code')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        session['username'] = username

        cursor.execute('select username, password from users')
        data = cursor.fetchall()

        for i in range(len(data)):
            if data[i][0] == username and data[i][1] == password:
                return render_template('admin.html')
            else:
                if i == len(data) - 1:
                    return Response('Invalid credentials , try again', mimetype='text/plain')

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('main'))
if __name__ == '__main__':
    app.run(debug=True)
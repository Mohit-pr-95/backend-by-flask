from flask import Flask, request, redirect, url_for, session, Response, render_template
import os
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

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

        users = {
            'mohit_95' : '3434',
            'mohish_87' : '6969',
            'duister_px' : 'pexos'
        }

        if username in users and password == users[username]:
            return render_template('user.html', name=username)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('main'))
if __name__ == '__main__':
    app.run(debug=True)
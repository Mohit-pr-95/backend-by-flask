from flask import Flask, request, redirect, url_for, session, Response, render_template
import os
from datetime import date
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
        else:
            return render_template('error.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('main'))

@app.route('/render_create_account')
def render_create_account():
    return render_template('create-account.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    if request.method == 'POST':
        username = request.form.get('create_username')
        password = request.form.get('create_password')
        confirm_password = request.form.get('confirm_password')

        users = {
            'mohit_95' : '3434',
            'mohish_87' : '6969',
            'duister_px' : 'pexos'
        }

        if confirm_password != password:
            return Response('Password doesnt match your created password, try again', mimetype='text/plain')
        else:
            if username in users:
                return render_template('username_already_exist.html')
            else:
                users[username] = password
                session['user'] = username
                return render_template('user.html', name=username)


if __name__ == '__main__':
    app.run(debug=True)
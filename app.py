from flask import Flask, request, redirect, url_for, session, Response, render_template
import os, dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('secret_code')

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    session['user'] = username
    
    if username == 'admin' and password == '123':
        return render_template('welcome.html')
    else:
        return Response('Invalid credentials, try again', mimetype='text/plain') # telling browser that what type of response we will return, # by default flask returns text/HTML page

@app.route('/logout')
def logout():
    session.pop('user')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# This will be our Flask app
from flask import Flask, redirect, url_for
import sqlalchemy

app = Flask(__name__)

@app.route('/home/')
def home():
    return "Hello this is the main page <h1>Project 2</h1>"

@app.route('/<name>/')
def user(name):
    return f'Hello {name}!'

@app.route('/admin/')
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug = True)
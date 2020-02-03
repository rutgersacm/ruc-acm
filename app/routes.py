from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/officers')
def officers():
    return render_template('officers.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

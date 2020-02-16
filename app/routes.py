from app import app
import csv
from flask import render_template, url_for


## Example loading data in from a file,
## to pass it into the achievements template.
achievementsList = []
with open('./app/static/data/test-achievement.csv', 'r') as achievementfile:
    file_reader = csv.reader(achievementfile, delimiter=',', quotechar='"')
    firstRow = False
    for row in file_reader:
        if not firstRow:
            firstRow = True
            continue
        achievementsList.append({
        'awardName':row[0],
        'name':row[1],
        'description':row[2]
        })

print(achievementsList)

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
    return render_template('achievements.html', achievementsList=achievementsList)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

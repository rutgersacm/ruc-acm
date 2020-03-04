from app import app
import csv
from flask import render_template, url_for, request, jsonify, make_response
import os
import time

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
        'description':row[2],
        'photoLink':row[3]
        })

print(achievementsList)

db = ["./static/images/chapter_photos/" + file for file in os.listdir("./app/static/images/chapter_photos")]
posts = len(db)
quantity = 4

#all_photos

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


## TODO Implement this...
@app.route("/load")
def load():
    """ Route to return the posts """

    time.sleep(0.2)  # Used to simulate delay

    if request.args:
        counter = int(request.args.get("c"))  # The 'counter' value sent in the QS

        if counter == 0:
            print(f"Returning posts 0 to {quantity}")
            # Slice 0 -> quantity from the db
            res = make_response(jsonify(db[0: quantity]), 200)

        elif counter == posts:
            print("No more posts")
            res = make_response(jsonify({}), 200)

        else:
            print(f"Returning posts {counter} to {counter + quantity}")
            # Slice counter -> quantity from the db
            res = make_response(jsonify(db[counter: counter + quantity]), 200)

    return res

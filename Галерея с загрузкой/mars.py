from flask import Flask, redirect, render_template, request
from random import choice
import json

app = Flask(__name__)
images = ['/static/img/mars1.jpg', '/static/img/mars2.jpeg', '/static/img/mars3.jpeg']


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    new = f'/static/img/mars{len(images) + 1}.jpg'
    if request.method == 'GET':
        return render_template('galery.html', images=images)
    elif request.method == 'POST':
        f = request.files['file']
        with open(new.lstrip('/'), "wb") as file:
            file.write(f.read())
        images.append(new)
        return render_template('galery.html', images=images)


@app.route('/')
def index():
    return redirect('/galery')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

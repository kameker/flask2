from base64 import b64encode

from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/carousel')
def greeting():
    return render_template('index.html')


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return render_template('load.html', title='Отбор астронавтов')
    elif request.method == 'POST':
        image = request.files['file']
        bytes = image.read()
        image = b64encode(bytes).decode('utf-8')
        with open("static/img/picture.txt", "w") as f:
            f.write(image)
            f.close()
        return render_template('load.html', title='Отбор астронавтов', image=image)


if __name__ == '__main__':
    app.run()

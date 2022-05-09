from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/carousel')
def greeting():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

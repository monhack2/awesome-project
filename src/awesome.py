from flask import Flask, render_template

app = Flask(__name__)


@app.route('/anime')
def anime():
    return render_template('anime.html', title='Anime')

@app.route('/')
def index():
    return render_template('index.html', title='Index')
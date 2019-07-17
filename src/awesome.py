from flask import Flask, render_template

app = Flask(__name__)


class page:
    def __init__(self, title, url):
        self.title = title
        self.url = url


@app.route('/')
def index():
    title = "Index"
    page_list = [page("Index", "/"), page("Gud Page", "/gudPage")]
    return render_template('index.html', **locals())


@app.route('/gudPage')
def gudPage():
    title = "Gud Page"
    page_list = [page("Index", "/"), page("Gud Page", "/gudPage")]
    return render_template('index.html', **locals())

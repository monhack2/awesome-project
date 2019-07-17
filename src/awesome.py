from flask import render_template
from .config import app
from .user import User


@app.route('/anime')
def anime():
    return render_template('anime.html', title='Anime')

@app.route('/')
def index():
    return render_template('index.html', title='Index')

  
@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', title='Users list', users=users)

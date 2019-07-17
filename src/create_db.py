from .config import db
from .user import User

db.create_all()
alice = User(username='Alice')
bob = User(username='Bob')
db.session.add(alice)
db.session.add(bob)
db.session.commit()

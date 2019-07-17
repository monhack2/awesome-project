from .config import db
from .user import User

db.create_all()
alice = User(username='Alice')
bob = User(username='Bob')
rafi = User(username='Rafi')
db.session.add(alice)
db.session.add(bob)
db.session.add(rafi)
db.session.commit()

from sqlalchemy import ForeignKey

from configuretion import *


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Integer, unique=True)
    contact = db.Column(db.String(100))
    email = db.Column(db.String(100))
    userId = db.Column(db.Integer, ForeignKey('users.id'))
    createdAt = db.Column(db.DateTime, default=datetime.now())
    updatedAt = db.Column(db.DateTime)

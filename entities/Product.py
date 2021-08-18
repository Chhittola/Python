from sqlalchemy import ForeignKey

from configuretion import *


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    categoryId = db.Column(db.Integer, ForeignKey('category.id'))
    code = db.Column(db.Integer, unique=True)
    unitPrice = db.Column(db.Float)
    unitInStock = db.Column(db.Integer)
    photo = db.Column(db.String(100))
    userId = db.Column(db.Integer, ForeignKey('users.id'))
    createdAt = db.Column(db.DateTime, default=datetime.now())
    updatedAt = db.Column(db.Date)

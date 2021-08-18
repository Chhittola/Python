from sqlalchemy import ForeignKey

from configuretion import *


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey('users.id'))
    saleDate = db.Column(db.DateTime, default=datetime.now())
    subTotal = db.Column(db.Float)

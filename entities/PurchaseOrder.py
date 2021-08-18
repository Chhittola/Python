from sqlalchemy import ForeignKey

from configuretion import *


class PurchaseOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, ForeignKey('product.id'))
    supplierId = db.Column(db.Integer, ForeignKey('supplier.id'))
    userId = db.Column(db.Integer, ForeignKey('users.id'))
    quantity = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.FLOAT(10, 2))
    subTotal = db.Column(db.FLOAT)

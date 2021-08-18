from configuretion import *
from sqlalchemy import ForeignKey, PrimaryKeyConstraint


class SaleDetail(db.Model):
    saleId = db.Column(db.Integer, ForeignKey('sale.id'))
    productId = db.Column(db.Integer, ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    unitPrice = db.Column(db.FLOAT, nullable=False)
    total = db.Column(db.FLOAT, default=unitPrice * quantity)
    __table_args__ = (
        PrimaryKeyConstraint(saleId, productId),
        {},
    )

import json

from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5433/testing'
db = SQLAlchemy(app)


class Product(db.Model):
    productId = db.Column(db.Float, primary_key=True)
    name = db.Column(db.String)
    barcode = db.Column(db.String)
    unitPrice = db.Column(db.Float)
    sellPrice = db.Column(db.Float)
    qty = db.Column(db.Integer)

    @staticmethod
    def Index():
        db.create_all()
        message = {"message": "Table Create"}
        return jsonify(message)

    @staticmethod
    def CreateProduct():
        data = request.get_json()
        obj = Product()
        obj.productId = data['id']
        obj.name = data['name']
        obj.barcode = data['barcode']
        obj.unitPrice = data['unitPrice']
        obj.sellPrice = data['sellPrice']
        obj.qty = data['qty']
        db.session.add(obj)
        db.session.commit()
        message = {"message": "Product Created"}
        return jsonify(message)

    @staticmethod
    def GetAllProducts():
        data = Product.query.all()
        result = []
        for col in data:
            product = {}
            product['productId'] = col.productId
            product['name'] = col.name
            product['barcode'] = col.barcode
            product['unitPrice'] = col.unitPrice
            product['sellPrice'] = col.sellPrice
            product['qty'] = col.qty
            result.append(product)
        return json.dumps(result)

    @staticmethod
    def GetProduct(product_id):
        product = Product.query.filter_by(productId=product_id).first()
        if not product:
            message = {"message": "Product Not Found"}
            return jsonify(message)
        obj = {}
        obj['productId'] = product.productId
        obj['name'] = product.name
        obj['barcode'] = product.barcode
        obj['unitPrice'] = product.unitPrice
        obj['sellPrice'] = product.sellPrice
        obj['qty'] = product.qty
        return make_response(jsonify(obj), 200)

    @staticmethod
    def DeleteProductById(product_id):
        product = Product.query.filter_by(productId=product_id).first()
        if not product:
            message = {"message": "Product Not Found"}
            return jsonify(message)
        db.session.delete(product)
        db.session.commit()
        return make_response(jsonify("The product id {product_id}".format(product_id=product_id)), 200)


app.add_url_rule("/", view_func=Product.Index)
app.add_url_rule("/", view_func=Product.CreateProduct, methods=['POST'])
app.add_url_rule("/getProducts", view_func=Product.GetAllProducts, methods=['GET'])
app.add_url_rule("/getProducts/<product_id>", view_func=Product.GetProduct, methods=['GET'])
app.add_url_rule("/delete/<product_id>", view_func=Product.DeleteProductById, methods=['DELETE'])

from flask import Flask
from configuretion import *
from entities.Users import *
from entities.Category import Category
from entities.Product import Product
from entities.PurchaseOrder import PurchaseOrder
from entities.Sale import Sale
from entities.SaleDetail import SaleDetail
from entities.Supplier import Supplier
from security.jwt_config import JWTConfig

app.add_url_rule("/user", view_func=Users.create_user, methods=["POST"])
app.add_url_rule("/user", view_func=Users.get_all, methods=["GET"])
app.add_url_rule("/user", view_func=Users.update_user, methods=["PUT"])
app.add_url_rule("/user/<public_id>", view_func=Users.delete_by_id, methods=["DELETE"])

app.add_url_rule("/login", view_func=JWTConfig.login, methods=["POST"])

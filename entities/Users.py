import json
import uuid

from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash

from configuretion import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean)
    status = db.Column(db.Boolean)
    address = db.Column(db.String(100))
    gender = db.Column(db.String(10))

    @staticmethod
    def create_user():
        request_data = request.get_json()
        user = Users()
        user.public_id = str(uuid.uuid4())
        user.name = request_data['name']
        hashed_password = generate_password_hash(request_data['password'], method='sha256')
        user.password = hashed_password
        user.admin = True
        db.session.add(user)
        db.session.commit()
        message = {"message": "User created"}
        return jsonify(message)

    @staticmethod
    def update_user():
        request_data = request.get_json()
        user = Users.query.filter_by(public_id=request_data['public_id']).first()
        if not user:
            return jsonify({"message": "user not found"})
        user.name = request_data['username']
        hashed_password = generate_password_hash(request_data['password'], method='sha256')
        user.password = hashed_password
        user.admin = request_data['admin']
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "updated"}), 202

    @staticmethod
    @jwt_required()
    def get_all():
        users = Users.query.all()
        results = []
        for col in users:
            user = {'id': col.id, 'username': col.name, 'public_id': col.public_id, 'password': col.password,
                    'admin': col.admin}
            results.append(user)
        return json.dumps(results)

    @staticmethod
    def delete_by_id(public_id):
        user = Users.query.filter_by(public_id=public_id).first()
        if not user:
            return jsonify({"message": "user not found"})
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "user has been deleted"})

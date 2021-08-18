from sqlalchemy import ForeignKey

from configuretion import *


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    userId = db.Column(db.Integer, ForeignKey('users.id'))
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    @staticmethod
    def create_category():
        request_data = request.get_json()
        category = Category()
        name = request_data['name']
        user_id = request_data['userId']
        created_at = datetime.now()
        exist_category = Category.query.filter_by(name=name).first()
        if exist_category:
            return jsonify({"message": f"category name {name} has already exists"})
        category.name = name
        category.userId = user_id
        category.createdAt = created_at
        db.session.add(category)
        db.session.commit()
        return jsonify({"message": f"category {name} created successfully"})

    @staticmethod
    def get_category():
        categories = Category.query.all()
        results = []
        for col in categories:
            category = {'Id': col.id, 'Name': col.name, 'CreateDate': col.createdAt}
            results.append(category)
        return json.dumps(results)

    @staticmethod
    def update_category(_id):
        request_data = request.get_json()
        category = Category.query.filter_by(id=_id).first()
        if not category:
            return jsonify({"message", f"category id {id} not found"}), 401
        name = request_data['name']
        updated_at = datetime.now()
        category.name = name
        category.updatedAt = datetime.now()
        db.session.add(category)
        db.session.commit()
        return jsonify({"message": f"Update successfully"}), 204

    @staticmethod
    def delete_category(_id):
        category = Category.query.filter_by(id=_id).first()
        if not category:
            return jsonify({"message", f"category id {id} not found"}), 401
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": f"Category id {id} has been deleted successfully"}), 204

    @staticmethod
    def find_by_id(_id):
        category = Category.query.filter_by(id=_id).first()
        if not category:
            return jsonify({"message", f"category id {id} not found"}), 401
        result = [
            {"id": category.id, "name": category.name, "createdAt": category.createdAt, "createdBy": category.userId}]
        return json.dumps(result)

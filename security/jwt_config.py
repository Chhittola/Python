from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies
from configuretion import *
from entities.Users import Users


class JWTConfig(object):
    @staticmethod
    def refresh_expiring_jwt(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            return response

    @staticmethod
    def login():
        user_request = request.get_json()
        name = user_request['name']
        password = user_request['password']
        user = Users.query.filter_by(name=name, admin=True).first()
        if not user:
            return jsonify({"msg": "Bad username or password"}), 401
        if not check_password_hash(user.password, password):
            return jsonify({"msg": "Bad username or password"}), 401
        response = jsonify({"msg": "login successful"})
        access_token = create_access_token(identity=user.public_id)
        set_access_cookies(response, access_token)
        results = [{
            'access_token': access_token
        }]
        return json.dumps(results), 200

    @staticmethod
    def logout():
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response

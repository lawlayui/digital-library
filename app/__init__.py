from flask import Flask, request, jsonify, g, url_for
from .config import Config
from .blueprints import register_all_blueprint
from .core.db import db_close
from .core.security import verify_jwt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_all_blueprint(app)
    app.teardown_request(db_close)

    @app.before_request
    def verify_token():
        free_route = ['users.login', 'users.register']
        target = request.endpoint
        auth_header =request.headers.get('Authorization')
        token = None

        if target == 'static' or target == 'options' or target in free_route:
            return None

        if not auth_header:
            return jsonify({
                'status': 'error',
                'message': 'Missing header'
            })

        if target not in free_route:
            token = auth_header.split('Bearer ')[-1]
            
            try: 
                claims = verify_jwt(token)
                g.user_data = claims['data']
                return None

            except ValueError as e:
                return jsonify({
                    'status': 'error',
                    'message': str(e)
                })
            


    return app
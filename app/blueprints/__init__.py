from .auth import auth_bp 


def register_all_blueprint(app):
    app.register_blueprint(auth_bp, url_prefix='/api')
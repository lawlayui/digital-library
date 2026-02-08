from .users import users_bp

def register_all_blueprint(app):
    app.register_blueprint(users_bp, url_prefix='/api/user')
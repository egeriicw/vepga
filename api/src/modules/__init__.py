from src.modules.users import users_blueprint
from src.modules.auth import api as authApi

def initiate_app(app, **kwargs):
    app.register_blueprint(users_blueprint)
    app.register_blueprint(authApi)
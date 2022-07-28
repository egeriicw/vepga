from src.modules.users import users_blueprint
from src.modules.auth import api as authApi
from src.modules.accounts import accounts_blueprint

def initiate_app(app, **kwargs):
    app.register_blueprint(accounts_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(authApi)
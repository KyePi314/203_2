## The init file ##
from flask import Flask
from flask_login import LoginManager


# Put database stuff in here

def create_app():
    app = Flask(__name__)
    # @login_manager.user_loader
    ## Add user database stuff in here once database is connected
    # def load_user(user_id):
     #   return User.query.get(int(user_id))

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
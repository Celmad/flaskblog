from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# configs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f04516615517d8dbf6f9e4392faeec0e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # function name of route
login_manager.login_message_category = 'info'

# to avoid circular imports
from flaskblog import routes
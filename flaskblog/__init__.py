from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# configs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f04516615517d8dbf6f9e4392faeec0e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# to avoid circular imports
from flaskblog import routes
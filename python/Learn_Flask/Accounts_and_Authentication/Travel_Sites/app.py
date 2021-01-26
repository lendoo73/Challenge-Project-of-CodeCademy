from flask import Flask
# ------- Setup the database -------
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ------- Managing logged in state -------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # The name of the view to redirect to when the user needs to log in. 


import routes, models

# Initializing the database
#db.create_all()
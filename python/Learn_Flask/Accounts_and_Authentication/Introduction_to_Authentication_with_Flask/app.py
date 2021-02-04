import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask import request, render_template, flash, redirect, url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


app = flask.Flask(__name__)
app.secret_key = 'secretkeyhardcoded'
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
    
@app.route('/', methods = ['GET', 'POST'])
def index():
  if flask.request.method == 'GET':
    return '''
    <p>Your credentials: 
    username: TheCodeLearner
    password: !aehashf0qr324*&#W)*E!</p>
    <form action='/' method='POST'>
    	<input type='text' name='email' id='email' placeholder='email' />
        <input type='password' name='password' id='password' placeholder='password' />
        <input type='submit' name='submit' />
    </form>
    '''
  email = "TheCodeLearner"
  if flask.request.form['password'] == "!aehashf0qr324*&#W)*E!":
    user = User(email = "TheCodeLearner@gmail.com", username = "TheCodeLearner", password = "!aehashf0qr324*&#W)*E!")
    login_user(user)
    return render_template("logged_in.html", current_user = user )
  return login_manager.unauthorized()

@app.route('/home')
@login_required
def home():
	return render_template('logged_in.html')

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return "You are not logged in. Click here to get <a href="+ str("/")+">back to Landing Page</a>"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

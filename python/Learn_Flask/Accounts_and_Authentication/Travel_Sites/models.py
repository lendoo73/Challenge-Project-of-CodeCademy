from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
    
# ------- Create the User Model -------
class User(db.Model, UserMixin):
  id = db.Column(
    db.Integer, 
    primary_key = True
  )
  username = db.Column(
    db.String(50),
    index = True,
    unique = True
  )
  email = db.Column(
    db.String(120),
    unique = True,
    index = True
  )
  password_hash = db.Column(
    db.String(128)
  )
  posts = db.relationship(
    "Post",
    backref = "author",
    lazy = "dynamic"
  )
  
  def __repr__(self):
        return '<User {}>'.format(self.username)
  # ------- Creating Accounts and Authentication -------
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)   # return True or False

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String(140))
    country = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)
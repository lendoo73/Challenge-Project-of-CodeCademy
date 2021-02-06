from app import app, db
from flask import request, render_template, flash, redirect, url_for
from models import User, Post
from forms import RegistrationForm, LoginForm, DestinationForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/login', methods=['GET', 'POST'])
def login():
  #check if current_user logged in, if so redirect to a page that makes sense
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username = form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash("Invalid username or password")
      return redirect(url_for('login'))
    login_user(user, form.remember_me.data)
    next_page = request.args.get("next")
    if not next_page or url_parse(next_page).netloc != "":
      next_page = url_for("index")
    return redirect(next_page)
  return render_template('login.html', title = 'Sign In', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
  #check if current_user logged in, if so redirect to a page that makes sense
  if current_user.is_authenticated:
    return redirect(url_for("index"))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(
      username = form.username.data, 
      email = form.email.data
    )
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('login'))
  return render_template('register.html', title = 'Register', form = form)

@app.route('/user/<username>', methods = ['GET', 'POST'])
@login_required          # Protecting our pages
def user(username):
	user = current_user
	user = User.query.filter_by(username = user.username).first()
	posts = Post.query.filter_by(user_id = user.id)
	if posts is None:
		posts = []
	form = DestinationForm()
	if request.method == 'POST' and form.validate():
		new_destination = Post(
      city = form.city.data,
      country = form.country.data,
      description = form.description.data, 
      user_id = current_user.id)
		db.session.add(new_destination)
		db.session.commit()
	else:
		flash(form.errors)
	return render_template('user.html', user = user, posts = posts, form = form)

@app.route('/')
def index():
  posts = Post.query.all()
  if not posts:
    posts=[]
  return render_template('landing_page.html',posts = posts)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("login"))


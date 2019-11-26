from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST']) # allow these methods
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # First, I will hash the password to store it safely
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Then, I will create a new User model with the data of the register form, to store it in the DB
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        # Add user to DB and commit changes
        db.session.add(user)
        db.session.commit()
        # Give feedback to the user
        flash(f'Your account has been created {form.username.data}! You are now able to log in', 'success') # second argument is category, passing a bootstrap 4 class
        return redirect(url_for('login')) # passing name of function, not of route
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # login_user accepts a second argument, we will pass the 'remember me' checkbox value
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash(f'Unsuccessful. Email or password might be incorrect. Please, try again.', 'danger ')
    return render_template('login.html', title='Login', form=form)
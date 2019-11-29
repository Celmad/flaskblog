import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # login_user accepts a second argument, we will pass the 'remember me' checkbox value
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Unsuccessful. Email or password might be incorrect. Please, try again.', 'danger ')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    # Doesn't take any argument, cause it knows what user is logged in
    logout_user()
    return redirect(url_for('home'))


def save_photo(form_photo):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_photo.filename)
    photo_filename = random_hex + f_ext
    photo_path = os.path.join(app.root_path, 'static/profile_photos', photo_filename)
    output_size = (250, 250)
    # resizing image
    image = Image.open(form_photo)
    image.thumbnail(output_size)
    image.save(photo_path)
    return photo_filename


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.profile_photo.data:
            photo_file = save_photo(form.profile_photo.data)
            current_user.photo_profile = photo_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been updated', 'success')
        return redirect(url_for('account')) # redirecting here so that the render template below doesn't try to submit form again
    elif request.method == 'GET':
        # to populate form with current data
        form.username.data = current_user.username
        form.email.data = current_user.email
    photo_profile = url_for('static', filename='profile_photos/' + current_user.photo_profile)
    return render_template('account.html', title='Account', photo_profile=photo_profile, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form)


from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm # ,RequestResetForm, ResetPasswordForm
from flaskblog.users.utils import save_photo #, send_reset_email

# similar to "Flask(__name__)" but passing the name of the Blueprint as well
users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST']) # allow these methods
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
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
        return redirect(url_for('users.login')) # passing name of function, not of route
    return render_template('register.html', title='Register', form=form) # last argument is to pass it to pass data to the template


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # login_user accepts a second argument, we will pass the 'remember me' checkbox value
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Unsuccessful. Email or password might be incorrect. Please, try again.', 'danger ')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    # Doesn't take any argument, cause it knows what user is logged in
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
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
        return redirect(url_for('users.account')) # redirecting here so that the render template below doesn't try to submit form again
    elif request.method == 'GET':
        # to populate form with current data
        form.username.data = current_user.username
        form.email.data = current_user.email
    photo_profile = url_for('static', filename='profile_photos/' + current_user.photo_profile)
    return render_template('account.html', title='Account', photo_profile=photo_profile, form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)
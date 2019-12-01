import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_photo(form_photo):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_photo.filename)
    photo_filename = random_hex + f_ext
    photo_path = os.path.join(current_app.root_path, 'static/profile_photos', photo_filename)
    output_size = (250, 250)
    # resizing image
    image = Image.open(form_photo)
    image.thumbnail(output_size)
    image.save(photo_path)
    return photo_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='manuelalaminosd@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then just ignore this email.
'''
    mail.send(msg)
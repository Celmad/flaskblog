import os
import secrets
from PIL import Image
from flask import url_for, current_app
# from flask_mail import Message
# from flaskblog import mail

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
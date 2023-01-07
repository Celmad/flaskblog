Visit: mysimplepythonblog.com


INTRODUCTION

This web application has been developed as part of my degree at Edinburgh Napier University, especifically the Advance Web Tech module.

Requirements were to develop a web app with Python, using the Flask micro-framework, and it had to be deployed in a Ubuntu VM from their servers. Apart from that, we had quite a lot of freedom.


OVERVIEW & FEATURES

This is a simple Blog that accept user registrations and login. Users can create posts, update and delete them as well. Users can upload their profile picture and edit their profile.

In addition to that, users can request to update their password, in case they forget it.

From the usability point of view, a Dark Theme has been implemented.

The home and user's posts pages have a paging system, to reduce the amount of data requested at once and to avoid infinite scrolling.


PYTHON & FLASK

Python version 3.6.8 has been used, alongisde Flask version 1.1.1.

A number of Flask packages have been used, such as flask-bcrypt(password encryption), flask-login, flask-mail(to send password reset request), flask-sqlalchemy(ORM), flask-wtf + wtforms(forms), jinja2(templates) and pillow(processes images).


CSS & JAVASCRIPT

CSS variables have been used to store the different colours used in the web app, for better scalability.

The web app makes use of JavaScript to implement the Dark/Light theme toggle.


FRONT-END LIBRARIES

Bootstrap 4 is the main front-end library used. Font-Awesome was also used, which allowes the web app to have those specific icons you can see in the navigation bar and other places.


DEVELOPMENT ENVIRONMENT

Windows Linux Subsystem was the Operating System used for the development of this web application, with Ubuntu 18.04 LTS distribution.

VS Code in Windows 10 was the text editor of choice, accessing remotely to the WLS to develop in Python.

Windows 10 newest Terminal(Preview) app was used with the help of Bash shell in WLS to ssh into the Linux Ubuntu VM and be able to deploy this web application.

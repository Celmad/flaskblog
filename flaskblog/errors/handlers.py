from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

# using app_errorhandler() instead of errorhanlder() so we can use it across the application
# instead of just this blueprint
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404 # second value is a status code in Flask


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403 # second value is a status code in Flask


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500 # second value is a status code in Flask

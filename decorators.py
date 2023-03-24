import flask
from functools import wraps

def login_required(f):
    ''' Demand authentication to access route
    Example:
    ```
        from flask import current_app as app
        @login_required
        @app.route('/')
        def index():
            return 'Protected route'
    ```
    '''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not flask.session.get("user"):
            return flask.redirect(flask.url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

from flask import session
from functools import wraps

def login_required(function):
    @wraps(function)
    def decorator(*args,**kwargs):
        user = dict(session).get('email',None)
        print(dict(session))
        if user:
            return function(*args,**kwargs)
        return 'Login to access features'
    return decorator

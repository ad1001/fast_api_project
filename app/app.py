
# The user details get print in the console.
# so you can do whatever you want to do instead
# of printing it
 
from flask import Flask, url_for, redirect,session
from authlib.integrations.flask_client import OAuth
from db import UOWManager, CreateDataBase
import os
from auth_decorator import login_required
 
app = Flask(__name__)
app.secret_key = 'secret key'
 
 
app.config['SERVER_NAME'] = 'localhost:5000'
os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
oauth = OAuth(app)
 
google = oauth.register(
    name='google',
    client_id='278792377886-53hdm5ov9gvq1itic47rbmom3gndl1cn.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    jwks_uri= "https://www.googleapis.com/oauth2/v3/certs",
    client_kwargs={'scope': 'openid email profile'},
)


@app.route('/')
@login_required
def hello_world():
    email=dict(session).get('email',None)
    if email:
            db.get_user_creds()
    return f'Hello {email}!'


@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo',token=token)
    user_info = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    uow = UOWManager()
    curr = uow.get_cursor()
    db = CreateDataBase(cursor=curr)
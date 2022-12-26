
# The user details get print in the console.
# so you can do whatever you want to do instead
# of printing it
 
from flask import Flask, url_for, redirect,session, request
from authlib.integrations.flask_client import OAuth
import os
from auth_decorator import login_required
import finnhub

from redis import Redis

r = Redis(
    host='redis',
    port=6379
    )
 
app = Flask(__name__)
app.secret_key = 'secret key'
finnhub_client = finnhub.Client(api_key="FINHUB_KEY")

os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
oauth = OAuth(app)
 
google = oauth.register(
    name='google',
    client_id='GOOGLE_CLIENT_ID',
    client_secret='GOOGLE_SECRET_ID',
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
        symbol = request.args.get('symbol') 
        if symbol == '' or not symbol:
                return f'Hello {email} please send a symbol to check value!'
        if r.exists(f'{symbol}'):
            return r.get(f'{symbol}')
        else:
            value = str(finnhub_client.company_profile2(symbol=symbol))
            if value == '{}':
                return value
            r.set(f'{symbol}',value)            
            return str(value)     

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
    session['email'] = user_info['email']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    
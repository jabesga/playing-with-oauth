from flask import render_template, flash, redirect, request, session, url_for
from app import app
from .forms import LoginForm
import requests
from .delegauth import Delegauth

delegauth = Delegauth()

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/authorize/<provider>')
def authorize(provider):
    return delegauth.login_with(provider)

@app.route('/callback/facebook')
def callback_fb():
    response = delegauth.callback(request, 'facebook')
    session['access_token'] = response['access_token']
    return redirect(url_for('index'))

@app.route('/fb/me/')
def fb_me():
    if 'access_token' in session:
        response_me = requests.get('https://graph.facebook.com/v2.5/me?fields=id,name,email',
        headers={'Authorization': 'OAuth {0}'.format(session['access_token'])})
        return str(response_me.json())
    else:
        return 'No access_token'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

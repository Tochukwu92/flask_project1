from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def index():
    user = {'name': 'Tochukwu Ilonuba'}
    posts = [
            {
                'author': {'name': 'John'},
                'content': 'A guy with big God!'
            },
            {
                'author': {'name': 'Mary'},
                'content': 'Jesus i love you!'
            }
            ]
    return render_template('index.html', title='Homie', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        remember_me = form.remember_me.data
        flash('You are logged in as {} remember_me={}'.format(username, remember_me), 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

"""Defines routes necessary for user authentication"""
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm, SignUpForm


@app.route('/')
@app.route('/index')
def index():
    user = "Tim"
    return render_template("index.html", user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Creates a login form route"""
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'
              .format(
                  form.email.data, form.remember_me.data
              ))
        return redirect('/index')
    return render_template('login.html', title='sign In', form=form)


@app.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    """Creates a sign up form"""
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'
              .format(
                  form.email.data, form.remember_me.data
              ))
        return redirect('/index')
    return render_template('signup.html', title='Sign Up', form=form)

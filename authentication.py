## For log in/sign up actions ##

## Importing important packages ###
from flask import (render_template, request, Blueprint, redirect, session, url_for, flash)
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, session

from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)
# Temp database info to get login stuff tpio run and load the home page

session = session

@auth.route('/login', methods=['GET', 'POST']) # Defining the login page path
def login(): # Log in page function
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(Username=name)
        if not user:
            flash('Account does not exist! Please sign up to continue')
            return redirect(url_for('auth.signup'))
        # elif not user and check_password_hash(user.Password, pwd):
        #     flash('Incorrect Password, please check your login details and try again')
        #     return redirect('auth.login')
        login_user(user)
        return redirect(url_for('main.home'))

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method ==  'GET':
        return render_template('auth/signup.html')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')
        email = request.form.get('email')
        user = User.query.filter_by(Email=email).first()
        if user:
            flash('Email is already in use with an existing account!')
            return redirect(url_for('auth.signup'))
        new_user = User(Email=email, Username=name, Password=pwd)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

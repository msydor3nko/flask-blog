# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from app import app, db
from flask import render_template, flash, redirect, url_for, request, jsonify
from app.forms import LoginForm, RegistrationForm, AnalyticsForm, PostCreationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import User, Post, PostLike


@app.route('/')
@app.route('/index')
@login_required  # redirect not log-in users to '/login' page and return back after log-in
def index():
    posts = Post.query.all()
    print('current_user', current_user)
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # authenticated user
    print('|> current_user | first => ', current_user)
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # user authentication form
    form = LoginForm()
    if form.validate_on_submit():   # POST-method -> True: handling form data | GET-method -> False: ommit form handling
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        # saving login into 'last_visit'
        user.last_visit = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password_one.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostCreationForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('New post created!')
        return redirect(url_for('create_post'))
    return render_template('post.html', title='New Post', form=form)


@app.route('/analytics', methods=['GET', 'POST'])
@login_required
def analyse_likes():
    # set default period
    date_to=datetime.today()
    date_from=date_to-timedelta(days=3)
    period = {"date_to": date_to.date(), "date_from": date_from.date()}
    
    form = AnalyticsForm()

    if form.validate_on_submit():
        # getting date period from the AnalyticsForm
        date_from = datetime.strptime(form.date_from.data, '%Y-%m-%d')
        date_to = datetime.strptime(form.date_to.data, '%Y-%m-%d')+timedelta(days=1)
        likes_period = PostLike.query.filter(PostLike.like == True)\
            .filter(PostLike.date >= date_from)\
            .filter(PostLike.date <= date_to)\
            .all()
        
        # summarise likes by days
        if not likes_period:
            flash('There is no likes for current period!')
            return redirect(url_for('analyse_likes'))

        likes_summary = {}
        for like in likes_period:
            date = str(like.date.date())
            likes_summary[date] = likes_summary.get(date, 0) + 1
        return jsonify(likes_summary)

    return render_template('analytics.html', title='Analytics', form=form, period=period)




# @app.before_request
# def log_request_info():
#     app.logger.debug('Headers: %s', request.headers)
#     app.logger.debug('Body: %s', request.get_data())




# print(f"=> user.is_authenticated    => {user.is_authenticated}")
# print(f"=> user.is_active           => {user.is_active}")
# print(f"=> user.is_anonymous        => {user.is_anonymous}")
# print(f"=> user.get_id()            => {user.get_id()}")
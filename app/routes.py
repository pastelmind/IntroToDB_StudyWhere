from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, reviewForm, registerForm
from app.models import *
from sqlalchemy import *


@app.route('/')
def home():
    return render_template('home.html', title='Exp')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.userid.data, form.remember_me.data))
        return redirect("/")
    return render_template('login.html', title='Sign In', form=form)


@app.route('/review', methods=['GET', 'POST'])
def review():
    review = reviewForm()
    if review.validate_on_submit():
        flash('Review requested for ReviewName {}, like_score={}'.format(
            review.reviewname.data, review.like_score.data))
        return redirect("/")

    return render_template('review.html', title='Review', form=review)


@app.route('/register', methods=['GET', 'POST'])
def register():
    register = registerForm()
    if register.validate_on_submit():
        flash(' ID: {}, 이름={} 님의 회원가입이 완료되었습니다.'.format(
            register.userid.data, register.username.data))
        return redirect("/")

    return render_template('register.html', title='Register', form=register)

@app.route('/location', methods=['GET','POST'])
def location():
    location = Location.search_locations_by_category(0)
    return render_template('locations.html', title='Locations', location = location)

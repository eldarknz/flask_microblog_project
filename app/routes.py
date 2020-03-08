# -*- coding: utf-8 -*-
from flask import render_template
from app import app_inst

@app_inst.route('/')
@app_inst.route('/index')
def index():
    user = {'username': 'Miguel Soldado'}
    posts = [
        {
            'author': {'username': 'John'},
            'body'  : 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body'  : 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body'  : 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

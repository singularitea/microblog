from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Ben'}
    posts = [
            { 
                'author' : {'username': 'Bob'},
                'body' : 'Rippa of a day in Perth'
            },
            {
                'author' : {'username': 'Alice'},
                'body' : 'District 9, more like District Spline'
            }
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    

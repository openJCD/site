from flask import render_template, url_for
from DofE_Site import app

posts = [
    {
        'title':'First Image',
        'image_url':'DofE_Site/static/sunset_placeholder.JPG',
        'description':'The first image to be uploaded.'
    }
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/featured')
def featured():
    return render_template("featured.html")

@app.route('/about')
def about():
    return render_template("about.html")
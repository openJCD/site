from flask import render_template, url_for
from DofE_Site import app

posts = [
    {
        'title':'First Image',
        'image_url':'/static/sunset_placeholder.JPG',
        'description':'The first image to be uploaded.',
        'modal_id':'modal-1'
    }
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/featured')
def featured():
    return render_template("featured.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")
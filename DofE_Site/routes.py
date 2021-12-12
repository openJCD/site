from flask import render_template, url_for
from DofE_Site import app

posts = [
    {
        'title':'First Image',

        'image_url':'/static/sunset_placeholder.JPG',

        'description':'The first image to be uploaded.',

        'grid-placement':'grid-columns:1/1;grid-rows:1/1;',

        'portfolio-object':'square',

        'modal_id':'modal-1'
    },
    {
        'title':'Second Image',

        'image_url':'/static/seagull_wales.JPG',

        'description':'The second image to be uploaded.',

        'grid-placement':'grid-columns:2/2;grid-rows:1/1;',

        'portfolio-object':'rect',

        'modal_id':'modal-2'
    },
        {
        'title':'Third Image',
        'image_url':'/static/seagull_wales.JPG',
        'description':'The third image to be uploaded.',
        'modal_id':'modal-3'
    }
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/featured')
def featured():
    return render_template("featured.html", posts=posts)

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

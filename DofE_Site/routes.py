from flask import render_template, url_for, request, flash, redirect

from DofE_Site import app

posts = [
    {
        'title':'A Nice Sunset',

        'image_url':'/static/sunset_placeholder.JPG',

        'description':'The first image to be uploaded.',

        'modal_id':'modal-1',

        'is_featured':'true'
    },
    {
        'title':'Seagull atop the Llandudno summit complex',

        'image_url':'/static/seagull_wales.JPG',

        'description':'The second image to be uploaded.',

        'modal_id':'modal-2',

        'is_featured':'true'
    },
    {
        'title':'JCD logo',

        'image_url':'/static/JCD_modern.png',

        'description':'The fourth image to be uploaded.',

        'modal_id':'modal-4',

        'is_featured':'false',
    },
    {
        'title':'Two trees of contrasting age in Ickworth Park',

        'image_url':'/static/ickworth_tree.JPG',

        'description':'-generic-',

        'modal_id':'modal-5',

        'is_featured':'true'
    },
        {
        'title':'Macro picture of a leaf - not entirely sure why',

        'image_url':'/static/leaf.JPG',

        'description':'-generic-',

        'modal_id':'modal-6',

        'is_featured':'true'
    },
]

def get_posts_by_tag(tag, posts):
    sorted_posts=[]
    
    for post in posts:
        if tag in post and post[tag] =='true':
            sorted_posts.append(post)
        
    return sorted_posts


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/featured')
def featured():
    return render_template("featured.html", featured_posts=get_posts_by_tag('is_featured', posts))

@app.route('/portfolio')
def portfolio():     
    return render_template("portfolio.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/form_test_page_1", methods=('GET', 'POST'))
def test():
    if request.method == 'POST':
        red_tag = request.form['red_tag']
        flash( str(red_tag) )
        return(redirect(url_for('test')))

    return render_template("test.html")
from flask import Flask

app = Flask(__name__)

post_data = open(file="DofE_Site/posts.txt")

from DofE_Site import routes
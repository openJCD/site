from flask import Flask

import os

app = Flask(__name__)

app.secret_key=str(os.urandom(12))

from DofE_Site import routes
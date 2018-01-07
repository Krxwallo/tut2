import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# the toolbar is only enabled in debug mode:
#app.debug = True
# runserver.py does this for us

# set a 'SECRET_KEY' to enable the Flask session cookies
# we read the key from a file, which we exclude from
# the source repository
f=open(os.path.dirname(__file__)+"/flask_secret_key","r")
app.config['SECRET_KEY']=f.read()
f.close() 

toolbar = DebugToolbarExtension(app)

import tut2.views
import tut2.model

#Import packages
from flask import Flask
from flask_bcrypt import bcrypt
###from flask_ngrok import run_with_ngrok

#Create webapp instance
app = Flask(__name__)

### Having issues with ngrok
###run_with_ngrok(app)

app.config['SECRET_KEY'] = 'SecretKeyWillChangeForProduction'

import nlr_webapp.routes

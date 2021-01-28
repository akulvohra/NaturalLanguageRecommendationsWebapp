#Import packages
from flask import Flask

#Create webapp instance
app = Flask(__name__)

import nlr_webapp.routes

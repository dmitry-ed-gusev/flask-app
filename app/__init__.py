# -*- coding: utf-8 -*-

from flask import Flask
from config import Config

app = Flask(__name__)  # create a variable app as instance of class Flask in a module app

# loading application config from Config object
app.config.from_object(Config)

# other code here

from app import routes  # import routes from module app (last - to avoid circles)

# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)  # create a variable app as instance of class Flask in a module app

# other code here

from app import routes  # import routes from module app (last - to avoid circles)

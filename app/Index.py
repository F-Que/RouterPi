#coding:utf-8

from app import app
from flask.templating import render_template

@app.route('/index')
def index() :
    return render_template("test.html")
    
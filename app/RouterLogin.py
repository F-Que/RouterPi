#coding:utf-8
'''
Created on 2017年2月5日

@author: f-que
'''
from flask.templating import render_template
from app import  app
from flask.globals import request
import config
from werkzeug import redirect
from flask.helpers import url_for


@app.route('/login', methods = ['POST', 'GET'])
@app.route('/', methods = ['POST', 'GET'])
def routerLogin():
    errs = ''
    if request.method == 'POST':
        if request.form['input_pwd'] != config.ROUTER_PASSWORD:
            errs =  u"密码错误请重试"
        else:
            return redirect(url_for('index'))      
    return render_template("RouterLogin.html", errs = errs )
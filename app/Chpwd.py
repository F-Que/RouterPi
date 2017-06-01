#coding:utf-8
'''
Created on Jun 1, 2017

@author: que
'''
from app import app
from flask.globals import request
from flask.templating import render_template
from helper import FormHelper, SysConfigHelper, ItemGenerator
import hashlib

@app.route('/chpwd', methods = ['POST', 'GET'])
def chpwd():
    ls = ItemGenerator.genTitle('chpwd')
    errs = ''
    sucs = ''
    forms = FormHelper.getForm()
    if request.method == 'POST':
        form = request.form.to_dict()
        m1 = hashlib.md5()
        m1.update(form['input_opwd'])
        pwd = m1.hexdigest()
        if pwd != forms['pwd']:
            print pwd
            print forms['pwd']
            errs = u'密码错误请重试'
        elif form['input_npwd1'] != form['input_npwd2']:
            errs = u'新密码不匹配请重试'
        else:
            m2 = hashlib.md5()
            m2.update(form['input_npwd1'])
            forms['pwd'] = m2.hexdigest()
            FormHelper.setForm(forms)
            sucs = u'保存成功，重启后生效'
    return render_template('chpwd.html', 
                        s_status = ls['status'][0],
                        l_status = ls['status'][1],
                        s_hotpoint = ls['hotpoint'][0],
                        l_hotpoint = ls['hotpoint'][1],
                        s_port = ls['port'],
                        s_wanport = ls['wanport'][0],
                        l_wanport = ls['wanport'][1],
                        s_lanport  = ls['lanport'][0],
                        l_lanport = ls['lanport'][1],
                        s_dhcp = ls['dhcp'],
                        s_dhcps = ls['dhcps'][0],
                        l_dhcps = ls['dhcps'][1],
                        s_clist = ls['clist'][0],
                        l_clist = ls['clist'][1],
                        s_staticip = ls['staticip'][0],
                        l_staticip = ls['staticip'][1],
                        s_sysopt = ls['sysopt'],
                        s_sysrestart = ls['sysrestart'][0],
                        l_sysrestart = ls['sysrestart'][1],
                        s_chpwd = ls['chpwd'][0],
                        l_chpwd = ls['chpwd'][1],
                        errs = errs,
                        sucs = sucs) 
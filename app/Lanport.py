#coding:utf-8
'''
Created on 2017年2月6日

@author: f-que
'''
from app import app
from helper import FormHelper, SysConfigHelper
from helper import InterfaceHelper
from helper import ItemGenerator
from flask import render_template
from flask.globals import request


@app.route('/lanport', methods = ['POST', 'GET'])
def  lanport():
    ls =ItemGenerator.genTitle('lanport')
    errs = ''
    sucs = ''
    forms = FormHelper.getForm()
    if request.method == 'POST':
        forms['lanport'] = request.form.to_dict()
        errs = SysConfigHelper.setLan(forms)
        if errs == '': 
            FormHelper.setForm(forms)
            sucs = u'保存成功，重启后生效'
    return render_template("Lanport.html",
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
                            mac = InterfaceHelper.getNetworkInterFaces('wlan0')['mac'],
                            ip = forms['lanport']['input_ip'],
                            mask = forms['lanport']['input_mask'],
                            sucs = sucs,
                            errs = errs)
        
        
    
        
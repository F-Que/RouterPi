#coding:utf-8
'''
Created on 2017年2月7日

@author: f-que
'''
from app import app
from flask.globals import request
from flask.templating import render_template
from helper import FormHelper, SysConfigHelper, ItemGenerator

@app.route('/hotpoint', methods = ['POST', 'GET'])
def hotpoint():
    ls = ItemGenerator.genTitle('hotpoint')
    pwd = ''
    errs = ''
    sucs = ''
    forms = FormHelper.getForm()
    #print forms['hotpoint']['input_ssid']
    if request.method == 'POST':
        forms['hotpoint'] = request.form.to_dict()
        errs = SysConfigHelper.setHostapd(forms)
        if errs == '':
            FormHelper.setForm(forms)
            sucs = u'保存成功，重启后生效'
    if forms['hotpoint'].has_key('input_pwd'):
        pwd = forms['hotpoint']['input_pwd']
    return render_template('Hotpoint.html', 
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
                        ssid = forms['hotpoint']['input_ssid'],
                        channel = forms['hotpoint']['sel_channel'],
                        boardcast_checked = ItemGenerator.genCheckbox('hotpoint', 'ckb_boardcast'),
                        pwd_checked = ItemGenerator.genCheckbox('hotpoint', 'ckb_pwd'),
                        pwd_disabled = ItemGenerator.disableItem('hotpoint','input_pwd'),
                        pwd = pwd,
                        errs = errs,
                        sucs = sucs) 
    
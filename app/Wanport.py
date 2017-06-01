#coding:utf-8
'''
Created on 2017年2月12日

@author: f-que
'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
from app import app 
from flask.templating import render_template
from helper import ItemGenerator, FormHelper, InterfaceHelper, SysConfigHelper
from flask.globals import request



@app.route('/wanport', methods = ['POST', 'GET'])
def wanport():
    errs = ''
    sucs = ''
    ls = ItemGenerator.genTitle('wanport')
    forms = FormHelper.getForm();
    iface = InterfaceHelper.getNetworkInterFaces('eth0')
    if request.method == 'POST':
        tmp = request.form.to_dict()
        if tmp['current_page'] != '2':
            if tmp['input_dns1'] == '':
                tmp['input_dns1'] = InterfaceHelper.getGateway()
            if tmp['input_dns2'] == '':
                tmp['input_dns2'] = '0.0.0.0'
        for k in tmp:
            forms['wanport'][k] = tmp[k]
        errs = SysConfigHelper.setWan(forms)
        if errs == '':                  
            sucs = u'保存成功，请等待服务重启'
            FormHelper.setForm(forms)

    return render_template("Wanport.html", 
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
                            default_page = forms['wanport']['current_page'],
                            wan_ip = iface['ip'],
                            mask = iface['mask'],
                            gateway = InterfaceHelper.getGateway(),
                            dns1 = forms['wanport']['input_dns1'],
                            dns2 = forms['wanport']['input_dns2'],
                            pppname = 'username',
                            ppppwd = 'password',
                            ppp_connected = 'true',
                            sucs = sucs,
                            errs =errs)


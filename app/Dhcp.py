#coding:utf-8
'''
Created on Mar 27, 2017
@author: que
'''

from app import app
from helper import ItemGenerator, SysConfigHelper
from helper import FormHelper
from flask.templating import render_template
from flask.globals import request


@app.route('/dhcp', methods = ['POST', 'GET'])
def dhcp():
    ls = ItemGenerator.genTitle('dhcps')
    errs = ''
    sucs = ''
    forms =  FormHelper.getForm()
    if request.method == 'POST':
        forms['dhcp'] = request.form.to_dict()
        errs = SysConfigHelper.setDhcp(forms)
        if errs == '':
            if request.form.has_key('ckb_dhcp_on'):
                forms['dhcp'] = request.form.to_dict()
            elif forms['dhcp'].has_key('ckb_dhcp_on'):
                forms['dhcp'].pop('ckb_dhcp_on')
            sucs = u'保存成功，请等待服务重启'
            FormHelper.setForm(forms)
        
    return render_template('Dhcp.html', 
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
                            pool_start = forms['dhcp'].get('input_pool_start'),
                            pool_end = forms['dhcp'].get('input_pool_end'),
                            auto_lease = forms['dhcp'].get('input_auto_lease'),
                            dns1 =  forms['dhcp'].get('input_dns1'),
                            dns2 =  forms['dhcp'].get('input_dns2'),
                            sucs = sucs,
                            errs =  errs,
                            dhcp_on = ItemGenerator.genCheckbox('dhcp', 'ckb_dhcp_on'))

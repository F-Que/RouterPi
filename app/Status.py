#coding:utf-8
'''
Created on 2017年1月23日

@author: f-que
'''
from app import app
from helper import ItemGenerator,FormHelper,InterfaceHelper
from flask import render_template


@app.route('/status')
def status():
    wan = InterfaceHelper.getNetworkInterFaces('eth0')
    lan = InterfaceHelper.getNetworkInterFaces('wlan0')
    ls =  ItemGenerator.genTitle('status')
    forms = FormHelper.getForm()
    str = render_template("Status.html",
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
                             w_mac = wan['mac'],
                             w_ip = wan['ip'],
                             w_mask = wan['mask'],
                             l_mac = lan['mac'],
                             l_ip = lan['ip'],
                             l_mask = lan['mask'])
    
    return str
                             
                             
                             

                             
                             
                             

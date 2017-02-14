#coding:utf-8
'''
Created on 2017年1月23日

@author: f-que
'''
from app import app
from helper import ItemGenerator
from flask import render_template

@app.route('/status')
def status():
    ls =  ItemGenerator.genTitle('status')
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
                             rpiver = 'rpi',
                             appver = '0.0.1',
                             ssid = 'Fq-rpi',
                             channel = '6',
                             ssid_bc = 'start',
                             w_mac = 'w_mac',
                             w_ip = '192.168.0.107',
                             w_mask = '225.255.255.0',
                             l_mac = 'l_mac',
                             l_ip = '192.168.2.1',
                             l_mask = '225.255.255.0')
    
    return str
                             
                             
                             

                             
                             
                             

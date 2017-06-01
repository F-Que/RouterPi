#coding:utf-8
'''
Created on Apr 25, 2017

@author: que
'''
from app import app
from helper.iscdhcpleases import IscDhcpLeases
from flask.templating import render_template
from helper import ItemGenerator

@app.route('/clist')
def clist():
    ls =ItemGenerator.genTitle('clist')
    leases  = IscDhcpLeases('/var/lib/dhcp/dhcpd.leases')
    client_list=[]
    client_dict = leases.get_current()
    for k in client_dict:
        client_list.append(client_dict[k])
    return render_template('Clist.html', 
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
                            client_list = client_list)
    

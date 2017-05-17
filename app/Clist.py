#coding:utf-8
'''
Created on Apr 25, 2017

@author: que
'''
from app import app
from helper.iscdhcpleases import IscDhcpLeases
from flask.templating import render_template

@app.route('/clist')
def clist():
    leases  = IscDhcpLeases('/var/lib/dhcp/dhcpd.leases')
    client_list=[]
    client_dict = leases.get_current()
    for k in client_dict:
        client_list.append(client_dict[k])
    print client_list
    return render_template('Clist.html', client_list = client_list)
    

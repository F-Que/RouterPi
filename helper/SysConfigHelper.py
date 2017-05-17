#coding:utf-8
'''
Created on 2017年2月14日

@author: f-que
'''
import os
import IPy
import InterfaceHelper


from flask.templating import render_template
from helper import ipaddr
def setHostapd(forms):
    form = forms['hotpoint']
    if form.has_key('ckb_boardcast'):
        boardcast = '0'
    else:
        boardcast = '1'
        
    s = render_template('hostapd.conf', 
                          ssid = form['input_ssid'],
                          channel = form['sel_channel'],
                          pwd = form['input_pwd'],
                          boardcast = boardcast)
    
    try:
        with open('hostapd.conf', 'w') as fp:
            fp.write(s)
            fp.close()
    except Exception, e:
        return u'保存配置文件失败\n' + e
    #os.system('service hostapd restart')
    return ''
        
def setDhcp(forms):
    form = forms['dhcp']
    iface = InterfaceHelper.getNetworkInterFaces('wlan0')
    subnet = IPy.IP(iface['ip']).make_net(iface['mask']).strNormal(0)
        
    s = render_template('dhcpd.conf',
                        auto_lease = form['input_auto_lease'],
                        subnet = subnet,
                        mask = iface['mask'],
                        pool_start = form['input_pool_start'],
                        pool_end = form['input_pool_end'],
                        dns1 = form['input_dns1'],
                        dns2 = form['input_dns2'],
                        lan_ip =  iface['ip'],
                        boardcast_addr = iface['bcast']
                        )
    
    try:
        with open('dhcpd.conf', 'w') as fp:
            fp.write(s)
            fp.close()
    except Exception, e:
        return u'保存配置文件失败\n' + e
    
    if form.has_key('ckb_dhcp_on'):
        print "os.system('service dhcpd restart')"
    else:
        print "os.system('service dhcpd stop')"
    return ''
    
def setLan(forms):
    form =  forms['lanport']
    s = render_template('interfaces',
                        lan_ip = form['input_ip'],
                        maks = form['input_mask'])
    
    try:
        with open('interface', 'w') as fp:
            fp.write(s)
            fp.close()
    except Exception, e:
        return u'保存配置文件失败\n' + e
    
    print "os.system('service dhcpcd restart')"
    return ''

def setWan(forms):
    form = forms['wanport']
    if form['current_page'] != '2':
        if form['current_page'] == '0':
            s = render_template('dhcpcd.conf',
                                dns1 = form['input_dns1'],
                                dns2 = form['input_dns2'])
        else:          
            s = render_template('dhcpcd.conf',
                                ip_with_mask = ipaddr.IPNetwork(form['input_ip'] + '/' + form['input_mask']),
                                gtway = form['input_gateway'],
                                dns1 = form['input_dns1'],
                                dns2 = form['input_dns2'])
        try:
            with open('dhcpcd.conf', 'w') as fp:
                fp.write(s)
                fp.close()
        except Exception, e:  
            return u'保存配置文件失败\n' + e
    
        print "os.system('service dhcpcd restart')"
        return '' 
    
    else:
        return u'ppp设置\n'
            
    

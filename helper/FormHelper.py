#coding:utf-8
'''
Created on 2017年2月6日

@author: f-que
'''
import json
import hashlib
pwd = 'admin'
m = hashlib.md5()
m.update(pwd)

form_prest = {
    'pwd': m.hexdigest(),
    'lanport': {'input_ip': '192.168.0.1', 'input_mask': '255.255.255.0'},
    'hotpoint':{'input_ssid': 'RaspberryPi', 'sel_channel': 's1'},
    'wanport': {'input_ip': '', 'input_mask': '', 'input_dns2': '4.4.4.4', 'current_page': '0', 'input_dns1': '8.8.8.8', 'input_gateway': '', 'input_ppppwd': 'password', 'input_pppname': 'pppname'},
    'dhcp': {"ckb_dhcp_on": "on","input_pool_end": "192.168.2.200","input_dns2": "4.4.4.4","input_dns1": "8.8.8.8","input_auto_lease": "7200","input_pool_start": "192.168.2.10"}
} 

def setForm(forms):
    fp = open('forms.json', 'w')
    json.dump(forms, fp)
    fp.close()

def getForm(addr = None):          
    try: 
        with open('forms.json', 'r') as fp:  
            forms = json.load(fp)
            fp.close()
            for k in form_prest:
                if not forms.has_key(k):
                    forms[k] = form_prest[k]
    except Exception, e:
        print Exception,':',e
        forms = form_prest
    finally:
        if addr != None:
            return forms[addr]
        else:
            return forms



        
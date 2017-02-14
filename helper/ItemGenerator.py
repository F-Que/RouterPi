#coding:utf-8
'''
Created on 2017年1月23日

@author: f-que
'''
from helper import FormHelper

def genTitle(addr):
    list1 = {
            'status' : ['', '/status'],
            'hotpoint' : ['', '/hotpoint'],
            'wanport' : ['', '/wanport'],
            'lanport' : ['', '/lanport'],
            'dhcps' : ['', '/dhcp'], 
            'clist' : ['', '/clist'],
            'staticip' : ['', '/staticip'],
            'sysrestart' : ['', 'sysrestart'],
            'chpwd' : ['', 'chpwd'], 
            'port' : '',
            'dhcp' : '',
            'sysopt' : ''
             
        }
    
    list1[addr] = ['active', '#']
    if addr in ['wanport', 'lanport']:
        list1['port'] = 'active dropdown'
    elif addr in ['dhcps', 'clist', 'staticip']:
        list1['dhcp'] = 'active dropdown'
    elif addr in ['sysrestart', 'chpwd']:
        list['sysopt'] = 'active dropdown'
    return list1


def genCheckbox(form, ckb):
    forms = FormHelper.getForm(form)
    if forms.has_key(ckb):
        return 'checked'
    return ''

def disableItem(form, item):
    forms = FormHelper.getForm(form)
    if not forms.has_key(item):
        return 'disabled'
    return ''
        

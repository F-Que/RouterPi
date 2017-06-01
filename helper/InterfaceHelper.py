#coding:utf-8
'''
Created on 2017年2月6日

@author: f-que
'''

import subprocess
import re

def getNetworkInterFaces(iface):
    try:
        ifconfig = subprocess.Popen("ifconfig" + iface, stdout = subprocess.PIPE)
        output = ifconfig.stdout.read()
    except:
        output = ''
        
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    mask_pattern = re.compile('(Mask:%s)' % ipstr)
    ip_pattern = re.compile('(inet addr:%s)' % ipstr)
    bcast_pattern = re.compile('(Bcast:%s)' % ipstr)
    mac_pattern = re.compile('([0-9a-f]{1,2}[:]){5}([0-9a-f]{1,2})')
    pattern = re.compile(ipstr)
    try:
        ip = re.search(pattern,re.search(ip_pattern, output).group()).group()
    except:
        ip = None
    
    try:    
        mask = re.search(pattern,re.search(mask_pattern, output).group()).group()
    except:
        mask = None
    try:
        bcast = re.search(pattern,re.search(bcast_pattern, output).group()).group()
    except:
        bcast = None
    try:
        mac = re.search(mac_pattern, output).group()
    except:
        mac = None
    #ip = '192.168.2.1'
    #mac = '3c:46:d8:08:d6:dc'
    #bcast = '192.168.2.255'
    #mask = '255.255.255.0'
    return {'ip': ip, 'mac': mac, 'mask': mask, 'bcast': bcast}

def getGateway():
    cmd = 'ip route show | grep "default"'
    p = subprocess.Popen(cmd , stdout = subprocess.PIPE, shell = True)
    output = p.stdout.read()
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    gateway_patten = re.compile(ipstr)
    try:
        gateway = re.search(gateway_patten, output).group()
    except:
        gateway = None
    return gateway

def getDns():
    cmd = 'cat /etc/resolv.conf'    
    p = subprocess.Popen(cmd , stdout = subprocess.PIPE, shell = True)
    output = p.stdout.read()
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    dns_pattern = re.compile('(nameserver %s)' % ipstr)
    pattern = re.compile(ipstr)
    tmp = dns_pattern.findall(output)
    if len(tmp) >= 1:
        dns1 = re.search(pattern, tmp[0][0]).group()
    else:
        dns1 = '8.8.8.8'
    if len(tmp) >= 2:    
        dns2 = re.search(pattern, tmp[1][0]).group()
    else:
        dns2 = '4.4.4.4'
        
    return [dns1, dns2]
    
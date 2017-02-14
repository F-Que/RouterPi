#coding:utf-8
'''
Created on 2017年2月14日

@author: f-que
'''
import FormHelper
from flask.templating import render_template
def setHostapd(forms):
    form = forms['hotpoint']
    if form.has_key('ckb_boardcast'):
        boardcast = '0'
    else:
        boaedcast = '1'
        
    str = render_template('hostapd.conf', 
                          ssid = form['input_ssid'],
                          channel = form['sel_channel'],
                          pwd = form['input_pwd'],
                          boardcast = boardcast)
    
    try:
        with open('hostapd.conf', 'w') as fp:
            fp.write(str)
            fp.close()
    except Exception, e:
        return u'保存配置文件失败'
    finally:
        return ''     
        
            
            
    

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:58:11 2020

@author: tarak
"""


>>import glob,time

>>from datetime import datetime

>>dir=’/sys/bus/w1/devices/’

>>device_name=glob.glob(dir+’28*’)[0]

>>data_file=device_name+’/w1_slave’

>>def temp_data():
    
>> f=open(data_file,’r’)

>> lines=f.readlines()

>> f.close()

>> return lines

>>def temp_values():
    
>> lines=temp_data()

>> while lines[0].strip()[-3]!=’YES’:
    
>> time.sleep(0,2)

>> lines=temp_data()

>> equal_pos=lines[1].find(‘t=’)

>> if equal_pos != -1:
    
>> temp_string=lines[1][equal_pos+2:]

>> temp_c=float(temp_string)/1000.0

>> temp_f=temp_c*9.0/5.0+32.0

>> return temp_c,temp_f

>>c,f=temp_values()

>>dt=datetime.now()

>>print str(dt)

>>@route(‘/’)

>>def centigrade (g=c,k=f,):
    
>> c,f=temp_values()

>> return template (‘temp in centigrade={{c}} temp in fahrenheit={{f}}’,c=c,f=f)

>>run(host=’192.168.1.6’,port=80)
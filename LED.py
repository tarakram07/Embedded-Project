# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:36:12 2020

@author: tarak
"""

# Hello World

#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(18,GPIO.OUT)

#GPIO.output(18,True)

# Blinking LED

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

for i in range(0,20) :
    
GPIO.output(18,True)

time.sleep(1)

GPIO.output(18,False)
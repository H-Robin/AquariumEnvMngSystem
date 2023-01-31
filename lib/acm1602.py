# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 08:46:25 2023
LCD ACM1602NI
@author: nori3dogs
"""
import time
from machine import Pin, I2C

I2C_COMMAND = 0x00
I2C_DATA = 0x80
I2C_CLEAR = 0x01
I2C_HOME = 0x02
I2C_DISPLAY_ON = 0x0F
I2C_LCD_1STLINE = 0x00 + 0x80
I2C_LCD_2NDLINE = 0x40 + 0x80

class Acm1602(object):
    def __init__(self):
        self.addr = 0x50
        self.i2c = I2C(0, scl=Pin(3), sda=Pin(2), freq=100) # I2C1 SDA:GP2 I2C1 SCL:GP3 
        #  bus number set 1
        self.lcdinit()
        self.lcdcmd(I2C_CLEAR)
        self.lcdwrite("LCD INIT COMP!! ")
        
    def lcdinit(self):
        self.lcdcmd(0x38)
        self.lcdcmd(I2C_CLEAR)
        self.lcdcmd(I2C_DISPLAY_ON)
        
    def lcdclear(self):
        self.lcdcmd(I2C_CLEAR)
        time.sleep(0.2)  

    def lcd1stline(self):
        self.lcdcmd(I2C_LCD_1STLINE)
        time.sleep(0.2)  
        
    def lcd2ndline(self):
        self.lcdcmd(I2C_LCD_2NDLINE)
        time.sleep(0.2)  
        
    def lcdcmd(self,code):
        self.i2c.writeto_mem(self.addr, I2C_COMMAND, bytes([code & 0xFF]), addrsize=8)
        time.sleep(0.2)
    
    def lcddata(self,code):
        self.i2c.writeto_mem(self.addr, I2C_DATA, bytes([code & 0xFF]), addrsize=8)
        time.sleep(0.2)

    def lcdwrite(self,message):
        for text in message:
            self.i2c.writeto_mem(self.addr, I2C_DATA, bytes([ord(text) & 0xFF]), addrsize=8)
            time.sleep(0.02)
        
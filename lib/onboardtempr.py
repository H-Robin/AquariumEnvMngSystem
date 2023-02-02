# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 08:46:25 2023
OnBoard AD Temperature sensor
@author: nori3dogs
"""
import machine
import utime

class onBoardTempr:
    def __init__(self,adch):
        self.adch = adch
        self.rawdata = sensor_temp = machine.ADC(self.adch)
        # ADC Vmax = 3.3V
        # 16bit resolution = 65535
        self.conversionfactor = 3.3 / (65535)
    
    def getTemprData(self):
        # 温度を計算します。センサは27度を基準にしている
        # 温度センサの数値を27度から引いて計算します。
        # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
        # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
        return(27 - (self.rawdata.read_u16() * self.conversionfactor - 0.706)/0.001721)     
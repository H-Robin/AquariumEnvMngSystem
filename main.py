from machine import Pin
import machine
import onewire
import ds18x20
import time
import binascii
import time
import led
import acm1602
import onboardtempr

UPDATE_TIME_SEC = 1
ROOM_TEMPR_DISP_TIME_SEC = 1
ONWIRE_READ_DELAY_TIME_MS = 750
GreenLed = led.Led(25,1)

gpNoOneWire = machine.Pin(28) #GP22
print('DS18B20 class:  ') 
DS18B20Sensor = ds18x20.DS18X20(onewire.OneWire(gpNoOneWire))
print('Acm1602 class:  ') 
lcddev = acm1602.Acm1602(0,17,16)
print('Onboard temperature sensor class')
OnBoardTemprSensor = onboardtempr.onBoardTempr(4)

sensors = DS18B20Sensor.scan()
 
print('Found DS18B20: ', sensors)
GreenLed.Ledon() 
while True:
    #room temperature
    lcddev.lcdclear()
    
#    print('Onboard temperature sensor')
    message = "AquaEnvMngSys "
    lcddev.lcd1stline()
    lcddev.lcdwrite(message)  
    message = "RoomT:{:.2f} C".format(OnBoardTemprSensor.getTemprData())
    lcddev.lcd2ndline()
    lcddev.lcdwrite(message)
    time.sleep(ROOM_TEMPR_DISP_TIME_SEC)  
    lcddev.lcdclear()

    # water temperature
    DS18B20Sensor.convert_temp()
    time.sleep_ms(ONWIRE_READ_DELAY_TIME_MS)
    lineflg = 0    
    lcddev.lcdclear()
    SensNo = 1
    for device in sensors:
        s = binascii.hexlify(device)
        readable_string = s.decode('ascii')
        if lineflg == 0:
#           print('Sensor 1,SerialNo: {}'.format(readable_string))

            lcddev.lcd1stline()
            lineflg += 1
        else:
#            print('Sensor 2,SerialNo: {}'.format(readable_string))
            lcddev.lcd2ndline()
            lineflg = 0
#        print(DS18B20Sensor.read_temp(device))
        message = "WT{}:{:.2f} C".format(SensNo,DS18B20Sensor.read_temp(device))
        lcddev.lcdwrite(message)  
        GreenLed.Ledoff()
        time.sleep_ms(ONWIRE_READ_DELAY_TIME_MS)
        SensNo += 1
    time.sleep(UPDATE_TIME_SEC)




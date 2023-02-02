from machine import Pin
import machine
import onewire
import ds18x20
import time
import binascii
import time
import led
import acm1602

GreenLed = led.Led(25,1)



gpNoOneWire = machine.Pin(28) #GP22
print('DS18B20 class:  ') 
ds18b20_sensor = ds18x20.DS18X20(onewire.OneWire(gpNoOneWire))
print('Acm1602 class:  ') 
lcddev = acm1602.Acm1602(0,17,16)

sensors = ds18b20_sensor.scan()
 
print('Found DS18B20: ', sensors)
 
while True:
    ds18b20_sensor.convert_temp()
    time.sleep_ms(750)
    lineflg = 0
    lcddev.lcdclear()
    SensNo = 1
    for device in sensors:
        GreenLed.Ledon()
        s = binascii.hexlify(device)
        readable_string = s.decode('ascii')
        if lineflg == 0:
            print('Sensor 1,SerialNo: {}'.format(readable_string))

            lcddev.lcd1stline()
            lineflg += 1
        else:
            print('Sensor 2,SerialNo: {}'.format(readable_string))
            lcddev.lcd2ndline()
            lineflg = 0
        print(ds18b20_sensor.read_temp(device))
        message = "WT{}:{} C".format(SensNo,ds18b20_sensor.read_temp(device))
        lcddev.lcdwrite(message)  
        GreenLed.Ledoff()
        time.sleep_ms(300)
        SensNo += 1
    time.sleep(1)



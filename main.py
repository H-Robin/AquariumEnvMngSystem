from machine import Pin
import machine
import onewire
import ds18x20
import time
import binascii
import time
import led

GreenLed = led.Led(25,1)



gpNoOneWire = machine.Pin(4) #GP4
 
ds18b20_sensor = ds18x20.DS18X20(onewire.OneWire(gpNoOneWire))
 
sensors = ds18b20_sensor.scan()
 
print('Found DS18B20: ', sensors)
 
while True:
    ds18b20_sensor.convert_temp()
    time.sleep_ms(750)
    cnt = 0
    for device in sensors:
        cnt += 1
        GreenLed.Ledon()
        s = binascii.hexlify(device)
        readable_string = s.decode('ascii')
        print('DeviceNo:{},SerialNo: {}'.format(cnt,readable_string))
        print(ds18b20_sensor.read_temp(device))
        GreenLed.Ledoff()
        time.sleep_ms(300)
    time.sleep(1)

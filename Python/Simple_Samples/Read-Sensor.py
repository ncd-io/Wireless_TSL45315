import time
import serial

# Change this serial port to the serial port you are using.
s = serial.Serial('/dev/ttyS0', 9600)

while True:
    packet_ready = s.read(1)
    if(ord(packet_ready) == 126):
        while s.inWaiting() < 28:
            time.sleep(.001)
        bytes_back = s.read(28)
        if(ord(bytes_back[14]) == 127):
            print('The packet has a data payload: ' + str(ord(bytes_back[14])))
            print('The packet is for sensor type: '+str(ord(bytes_back[21])))
            if(ord(bytes_back[21]) == 10):
                lux = (ord(bytes_back[24]) << 16) | (ord(bytes_back[25]) << 8) | (ord(bytes_back[26]))
                lux = lux / 100
                battery = ord(bytes_back[17]) << 8 | ord(bytes_back[18])
                voltage = 0.00322 * battery
                print('Sensor Number: '+str(ord(bytes_back[15])))
                print('Firmware Version: '+str(ord(bytes_back[16])))
                print('Lux: ' + str(lux))
                print('Battery Raw ADC: '+str(battery))
                print('Battery Voltage: '+str(voltage))

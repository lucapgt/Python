import serial
from time import sleep
import csv

VZ = "\x02\x56\x5A\x78\x01\x43\xF4\xFC\xA6\x0C\xA5\x75\x5A\x37\xE3\xCC\x03".encode()
P1 = "\x02\x50\x31\x7F\x03".encode()
V1 = "\x02\x56\x31\x54\xCC\x03".encode()
VZpar = "\x02\x56\x5A\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x03".encode('latin-1')
T2 = "\x02\x54\x32\x7A\x03".encode('latin-1')


ser = serial.Serial ("com5", 38400, 8, "N", 1, timeout=1)


ser.write (P1)
rxData = ser.read(2048).hex()
rxDt = rxData
print(rxDt)


for x in range(0,100):

    ser.write(P1)
    H1 = ser.read(1024).hex()
    print(H1)
    ser.write(T2)
    R2 = ser.read(1024).hex()
    print(R2)






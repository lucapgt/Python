import serial
from time import sleep
import csv

VZ = "\x02\x56\x5A\x78\x01\x43\xF4\xFC\xA6\x0C\xA5\x75\x5A\x37\xE3\xCC\x03".encode()
P1 = "\x02\x50\x31\x7F\x03".encode()
V1 = "\x02\x56\x31\x54\xCC\x03".encode()
VZpar = "\x02\x56\x5A\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x03".encode('latin-1')
print(VZpar.hex())
outputFile = open('test_field_drop_2sv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter=' ', lineterminator='\n')

ser = serial.Serial ("com5", 38400, 8, "N", 1, timeout=5)


ser.write (P1)
rxData = ser.read(2048).hex()
rxDt = rxData
print(rxDt)


for x in range(0,1000000):

    ser.write(VZ)
    resVZ = ser.read(2048).hex()
    print(resVZ)
    ser.write(V1)
    H1V1 = (x, "F", "-", ser.read(2048).hex())
    print(H1V1)
    outputWriter.writerow(H1V1)

    ser.write(VZpar)
    resVZpar = ser.read(2048).hex()
    print(resVZpar)
    ser.write(V1)
    H1V1par = (x, 'H', "-", ser.read(2048).hex())
    print(H1V1par)
    outputWriter.writerow(H1V1par)
    outputFile.tell()

outputFile.close()

import serial
from time import sleep
import csv

VZ = "\x02\x56\x5A\x78\x01\x43\xF4\xFC\xA6\x0C\xA5\x75\x5A\x37\xE3\xCC\x03".encode()
P1 = "\x02\x50\x31\x7F\x03".encode()
V1 = "\x02\x56\x31\x54\xCC\x03".encode()
VZpar = "\x02\x56\x5A\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x03".encode('latin-1')
COMANDO = "$01".encode()

outputFile = open('VW_REMOTE_TASTO_01_d4.csv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter=' ', lineterminator='\n')

ser = serial.Serial ("com43", 115200, 8, "N", 1, timeout=None)




for x in range(0,10000):

    ser.write(COMANDO)
    buf = ser.in_waiting
    print(buf)
    while buf < 21:
        buf = ser.in_waiting
        print(buf)

    resCOMANDO = (ser.read((19)).decode('utf-8'))
    print(resCOMANDO)
    resCOMANDOconv = resCOMANDO
    outputWriter.writerow(resCOMANDOconv)
    ser.flushInput()
    sleep(1)
    outputFile.tell()


outputFile.close()

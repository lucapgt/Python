import serial
from time import sleep
import csv

VZ = "\x02\x56\x5A\x78\x01\x43\xF4\xFC\xA6\x0C\xA5\x75\x5A\x37\xE3\xCC\x03".encode()
P1 = "\x02\x50\x31\x7F\x03".encode()
V1 = "\x02\x56\x31\x54\xCC\x03".encode()
VZpar = "\x02\x56\x5A\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x03".encode()
PG = '\x02\x50\x47\x7E\x0A\x7E\x10\x83\x80\x01\xAF\x54\x8C\x04\x2E\x99\x0A\x7E\x10\x83\x80\x01\x17\x4C\x8C\x08\x42\x53\x0A\x7E\x10\x83\x80\x01\xAF\x54\x8C\x0E\x74\x36\x0A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x0A\x7E\x80\x00\x00\x00\x00\x00\x20\x1F\xD0\x0A\x7E\x80\x00\x00\x00\x00\x00\x24\x3B\x96\x0A\x7E\x80\x00\x00\x00\x00\x00\x28\x57\x5C\x0A\x7E\x80\x00\x00\x00\x00\x00\x2C\x73\x1A\x0A\x7E\x00\x46\x01\xAF\x54\x8C\x78\x22\x97\x0A\x7E\xAF\x54\x8C\x0D\xAE\xBF\x10\x90\x20\x69\x0A\x7E\xAF\x54\x8C\x55\x99\x70\x10\x90\x27\x1A\x0A\x7E\xAF\x54\x8C\x7A\x43\xDA\x10\x90\x77\x89\x04\x00\x00\x09\x03'.encode('latin1')
#PG = '\xFF\x00\x80'.encode('latin1')

#PG1= (0x025047770A7E10838001AF548C042E990A7E10838001174C8C0842530A7E10838001AF548C0E74360A0000000000000000000000FFFFFFFFFFFFFFFFFFFF00FFFFFFFFFFFFFFFFFFFF0A7E800000000000201FD00A7E800000000000243B960A7E80000000000028575C0A7E8000000000002C731A0A7E004601AF548C7822970A7EAF548C0DAEBF109020690A7EAF548C5599701090271A0A7EAF548C7A43DA109077890400000903)
print("---------------------")
print("| Set mini on COM:5 |")
print("---------------------\n\n")
sleep(0.5)
print("-----------------------")
print("| insert new TK100-80 |")
print("-----------------------\n\n")
sleep(5)
print("wait...\n")

'''outputFile = open('test_field_drop_2sv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter=' ', lineterminator='\n')
'''
ser = serial.Serial ("com5", 115200, 8, "N", 1, timeout=16)


'''ser.write (P1)
rxData = ser.read(2048).hex()
rxDt = rxData
print(rxDt)'''


for x in range(0,1):

  '''  ser.write(VZ)
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

outputFile.close() '''
ser.write(P1)
read = ser.read(2048).hex()
print(read,"\n")
print("wait...\n")
#print(PG.hex())
sleep(1)
ser.write(PG)
#print(PG)
read1 = ser.read(2048).hex()
print(read1,"\n")
print("wait...\n")
sleep(1)
ser.write(P1)
read2 = ser.read(2048).hex()
print(read2)
sleep(10)
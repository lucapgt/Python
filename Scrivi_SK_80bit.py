import serial
from time import sleep
import csv

import serial.tools.list_ports

import tkinter
import tkinter as tk

import binascii



P1 = "\x02\x50\x31\x7F\x03".encode()
P2 = "\x02\x50\x32\x77\x0a\x7e\x10\x83\x80\x01\x7d\x57\x10\x83\x04\xe8\x63\x0a\x7e\x10\x83\x80\x01\x7d\x57\x10\x83\x08\x84\xa9\x0a\x7e\x10\x83\x80\x01\x7d\x57\x10\x83\x0e\xb2\xcc\x0a\xb3\xc9\x8c\x23\xec\xa5\x75\x5a\x37\xe3\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x0a\x7e\x80\x00\x00\x00\x00\x00\x20\x1f\xd0\x0a\x7e\x80\x00\x00\x00\x00\x00\x24\x3b\x96\x0a\x7e\x80\x00\x00\x00\x00\x00\x28\x57\x5c\x0a\x7e\x80\x00\x00\x00\x00\x00\x2c\x73\x1a\x0a\x7e\x08\x46\x01\x7d\x57\x10\x83\x7a\x1a\x90\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x47\x03".encode('latin-1')

P2Elmama = "025032770a7e10838001fc5f0d04ef0e0a7e10838001fc5f0d0883c40a7e10838001fc5f0d0eb5a10a587fa68a44a5755a37e300ffffffffffffffffffff00ffffffffffffffffffff0a7e800000000000201fd00a7e800000000000243b960a7e80000000000028575c0a7e8000000000002c731a0a7e084601fc5f0d7a1dfd00ffffffffffffffffffff00ffffffffffffffffffff00ffffffffffffffffffff0000000603"

P2enc = binascii.unhexlify(P2Elmama)


BI884_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'LPC USB VCom Port' in p.description
 ]

if not BI884_ports:
    raise IOError("No 884 found")
if len(BI884_ports) > 1:
    warnings.warn('Multiple 884 found - using the first')

print (BI884_ports[0])

ser = serial.Serial(BI884_ports[0])


ser.write (P1)

buf1 = ser.in_waiting+1
buf = ser.in_waiting
buf2 = 0
print("buf_first", buf)
while buf1 > buf:
    buf = ser.in_waiting
    while buf2 == 0:
        #sleep(0.01)
        buf2 = ser.in_waiting
        print("buf2", buf2)
    buf1 = ser.in_waiting
    print("buf", buf)
    print("buf1", buf1)




rxData = ser.read(buf).hex()
rxDt = rxData
print(rxDt)








class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "P2"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack(side="top")

        self.hi_there = tk.Label(text=rxDt, fg="blue").pack()



       # self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
       # self.quit.pack(side="bottom")

    def say_hi(self):
        ser.write(P2enc)
        print (P2enc.hex())
        sleep(3)

        buf1 = ser.in_waiting + 1
        buf = ser.in_waiting
        buf2 = 0
        print("buf_first", buf)
        while buf1 > buf:
            buf = ser.in_waiting
            while buf2 == 0:
                # sleep(0.01)
                buf2 = ser.in_waiting
                print("buf2", buf2)
            buf1 = ser.in_waiting
            print("buf", buf)
            print("buf1", buf1)

        rxData = ser.read(buf).hex()
        rxDt = rxData.encode()
        print(rxDt)
        #dataRXvar = StringVar()
        #dataRXvar.set(rxDt)
        self.hi_there = tk.Label(root, text=rxDt, fg="blue").pack()
        root.update_idletasks()







root = tk.Tk()
app = Application(master=root)
app.master.title("Comandi Mini")
app.mainloop()






















'''

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

outputFile = open('test_field_drop_2sv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter=' ', lineterminator='\n')

ser = serial.Serial ("com5", 115200, 8, "N", 1, timeout=16)


ser.write (P1)
rxData = ser.read(2048).hex()
rxDt = rxData
print(rxDt)


for x in range(0,1):

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

'''
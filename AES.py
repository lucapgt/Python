from Crypto.Cipher import AES
import binascii


#key = b'1324DA21825945A7D59E93D32C593ACE'
key = '\x13\x24\xDA\x21\x82\x59\x45\xA7\xD5\x9E\x93\xD3\x2C\x59\x3A\xCE'.encode('latin-1')


cipher = AES.new(key, AES.MODE_ECB)
data = '\x2e\x39\x7b\x3b\x29\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.encode('latin-1')
#data = '\x2e\x39\x7b\x3b\x29\x65\x00\x00\x36\xc2\x07\x32\xa0\x72\xb7\xaf'.encode('latin-1')

tx = "2e397b3b2965000036c20732a072b7af"

a = binascii.unhexlify(tx)

sk = binascii.unhexlify(input("SCRIVI SK HT2 (6byte):")) + (binascii.unhexlify("00000000000000000000"))
print (sk.hex())

print (a)

ciphertext = cipher.encrypt(sk)
print (key)
print (data)
print ("SK AES", ciphertext.hex())

cipherRealText = '\x71\xcb\x49\xa5\x15\xb2\xf1\xb8\xbe\x35\x43\xf3\x73\xdf\x8c\x57'.encode('latin-1')

testSK = binascii.unhexlify("3112F964A3243680D03B4251B9937478")
print ("TEST ", testSK.hex())

plaintxt = cipher.decrypt(testSK)
print (plaintxt.hex())

#padding sk: texas tutti 0, ht2 random, megamos 0c0d0e0f
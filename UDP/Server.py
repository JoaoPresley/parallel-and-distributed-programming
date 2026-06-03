#Servidor IP: 127.0.0.1
#porta:50000
import socket
import sys
HOST = '192.168.23.113'
PORT=50000
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serv = (HOST,PORT)
udp.bind(serv)
while True:
    msg,cliente = udp.recvfrom(1024)
    print(cliente,msg)
    udp.sendto (msg,cliente)
udp.close() #fecha o socket
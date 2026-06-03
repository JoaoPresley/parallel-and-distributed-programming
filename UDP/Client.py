#Cliente IP: endereço da maquina na rede
#Porta: Definida ao criar o processo
import socket
import sys
HOST = '127.0.0.1' #IP do servidor
PORT = 50000       #porta do servidor
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (HOST,PORT)
print('Para sair use CTRL + x\n')
msg = str.encode("0")
while msg != '\x18':
    msg = input()
    msg2 = str.encode(msg)
    udp.sendto(msg2,dest)
    msg3,srv = udp.recvfrom(1024)
    print(srv,msg3)
udp.close()

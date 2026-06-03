#Cliente TCP
#cd C:\UCDB\AulaUCDB\SD\Codigos\ICP

import socket
import sys

host = 'localhost'  #loopback 127.0.0.1
port = 50000 		#porta

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #criando socket IPV4 TCP
#com o soket criado vamos pedir uma conexão
c.connect((host,port))
#após conectar deve enviar dados para o servidor
msg=' '
while msg !='exit':
    msg = input()
    msg2 = str.encode(msg)
    #após conectar deve enviar dados para o servidor
    c.sendall(str.encode(msg))
    #após envio aguarda resposta do servidor, se tudo ocorrer
    #como esperado irá ecorar a mensagem enviada
    data = c.recv(1024)
    print('Mensagem ecoada: ',data.decode())
c.close()
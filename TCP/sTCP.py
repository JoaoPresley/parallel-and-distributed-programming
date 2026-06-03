#Servidor TCP
#cd C:\UCDB\AulaUCDB\SD\Codigos\ICP

import socket
import sys

host = 'localhost' 	#loopback
port = 50000 		#porta

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #criando socket IPV4 TCP
s.bind((host,port)) #ligando o socket na porta e endereço IPV4
s.listen() #o servidor fica escutando na porta 50000 e no endereço ip 127.0.0.1
print('Aguardando conexões!!!') #uma mensagem para ser impressa na tela
conn, ender = s.accept() #aceita as conexões e retorna as informações da conexão e portas
print ('Conectado em ',ender)
#loop para receber os dados e ecoar para o cliente conectado
while True:
		data = conn.recv(1024)
		print('dados recebidos: ',data.decode())
		if not data:
			print('Fechando a conexão!')
			conn.close();
			break
		conn.sendall(data)
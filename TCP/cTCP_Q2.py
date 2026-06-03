#Contexto: No arquivo ctcp.py, se o servidor for derrubado repentinamente, o cliente quebra abruptamente com uma exceção de rede.
#Tarefa: Altere o código do cliente TCP utilizando blocos try/except para torná-lo resiliente.
#Regra de Implementação: Envolva o envio e a recepção de mensagens em um bloco try. Se ocorrer um erro de conexão (como socket.error ou ConnectionResetError), o cliente deve capturar a exceção, imprimir a mensagem amigável "Conexão perdida com o servidor!" e encerrar o programa de forma limpa.

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
    try:
        c.sendall(str.encode(msg))
        # após envio aguarda resposta do servidor, se tudo ocorrer
        # como esperado irá ecorar a mensagem enviada
        data = c.recv(1024)
        if not data:
            raise ConnectionResetError
        print('Mensagem ecoada: ', data.decode())
    except (socket.error, ConnectionResetError):
        print('Conexão perdida com o servidor')
        break
c.close()
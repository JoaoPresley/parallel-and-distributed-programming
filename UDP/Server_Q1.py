#Contexto: No arquivo server.py original, o servidor aceita qualquer mensagem UDP e simplesmente a ecoa de volta para o cliente.
#Tarefa: Modifique o código do servidor UDP para que ele funcione como um validador de senha simples.
#Regra de Implementação: O servidor deve verificar a mensagem recebida. Se o cliente enviar a string exatamente igual a "admin123", o servidor deve responder "Acesso Concedido". Para qualquer outra mensagem, o servidor deve responder "Acesso Negado".


#Servidor IP: 127.0.0.1
#porta:50000
import socket
import sys
#HOST = '192.168.23.113' Alteração para rodar apenas local
HOST = '127.0.0.1'
PORT=50000
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serv = (HOST,PORT)
udp.bind(serv)
while True:
    msg,cliente = udp.recvfrom(1024)
    #Converte mensagem para UTF8
    msg_recebida = msg.decode('utf-8').strip()
    print("Mesagem recebida: ", msg_recebida)
    if(msg_recebida == "admin123"):
        resp = "Acesso concedido"
    else:
        resp = "Acesso negado"

    udp.sendto (resp.encode('utf-8') , cliente)
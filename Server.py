'''
SERVER

nesse modulo serao implementados a sacola de dados e os trabalhadores

Sacola de tarefas:

- recebe as tarefas enviadas pelo cliente e escalona as tarefas que serao operadoas pelos trabalhadores.
- recebe o retorno dos trabalhadores antes de enviar os valores para o cliente.
- a main do nosso servidor vai conter a sacola de tarefas

Trabalhadores:
- cada trabalhador é uma thread
- os trabalhadores recebem como parametros uma tupla de duas listas (uma linha e uma coluna)
- o retorno de cada trabalhador é uma tupla com o indice e o resultado da multiplicacao linha x coluna

'''

import socket, threading, time
from pickle import loads, dumps
from Worker import Worker


def matprod(id, row, col):    #essa funçao vai realizar o produto de uma linha e uma coluna
                              #seus parametros sao a posiçao que ela vai ocupar e duas listas
                              #a primeira eh a lista e a segunda a coluna

    nval = len(row)
    c = 0

    for i in range (nval):
        c += row[i]*col[i]

    print (id, c)


def main():
    
    
    host = 'localhost'                 #ip local
    port = 6080                        #porta do servidor

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # define o objeto socket

    sock.bind((host, port))  # reserva o 'endereco' de acesso do cliente ao servidor
    sock.listen(1)  # permite que o servidor seja acessado apenas por 1 cliente

    stdoutmutex = threading.Lock()
    threads = []
    bag = []
    res = []

        
    conn, cl_addr = sock.accept()  # objeto socket, endereco da conexao
    print("Conexao aceita.\nCliente: ", cl_addr)  # informa qual cliente que conectou (endereço do cliente)        
        
    while True:
        msg = conn.recv(1024)  # recebe mensagem do cliente
        if (loads(msg) == ''):
            break
        else:
            bag.append(loads(msg))


    for task in bag:

        thread = Worker(task,stdoutmutex)
        thread.start()
        threads.append(thread)

    for thread in threads:
        res.append(thread.join())

    conn.send(dumps(res))

    print('Enviando...')

    conn.send(dumps(bag))

    conn.close()

if __name__ == '__main__':
    main()

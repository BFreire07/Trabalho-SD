'''
CLIENTE

Vai receber as duas matrizes como parametro

A matriz A será mantida, enquanto a matriz B tera suas colunas transformadas em linhas (funcao transpose)
O cliente vai enviar uma tupla para a sacola de tarefas que esta no servidor

'''


import socket, time
from pickle import loads, dumps

def transpose(mat):      #essa funcao transforma as linhas da matriz
                         #em colunas e retorna uma nova matriz 'tmat'
    lis = []
    tmat = []

    row = len(mat)
    col = len(mat[0])

    for i in range(col):
        for j in range (row):
            lis.append(mat[j][i])
        tmat.append(lis)
        lis = []

    return tmat


def main():
    HOST = 'localhost'     # endereco ip do servidor
    PORT = 6080            # porta de acesso ao servidor

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um objeto socket
    dest = (HOST, PORT) #tupla com o destino da conexao
    tcp.connect(dest)   #conecta o cliente com o servidor

    matA = [[2,5,9,3,8],[4,3,3,2,1],[1,0,9,2,0],[1,5,4,5,4]]
    matB = [[2,1],[0,3],[2,3],[3,4],[5,4]]
    colB = transpose(matB)  #invoca a funcao transpose

    rxc = {}
    k = 0
    nrowA = len(matA)
    ncolB = len(colB)
    
    for i in range (nrowA):
        for j in range (ncolB):
            rxc = (matA[i],colB[j])
            k+=1
            tp = dumps(rxc)
            tcp.send(tp)
            time.sleep(0.1)
    
    tcp.send(dumps(''))

    print()
    
    res = tcp.recv(1024)
    res = loads(res)
    
    x = 0
    k = []
    for i in range(nrowA):
        lr = []
        for j in range(ncolB):
            lr.append(res[x])
            x += 1
        k.append(lr)

    print (k)
    print()
    print('Terminei')


if __name__ == "__main__":
    main()

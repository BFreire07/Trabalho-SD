import socket, time
from pickle import dumps, loads


class Client():
    def __init__(self, matA, matB, dest):
        self.matA = matA
        self.matB = matB
        self.dest = dest
        self.nrowA = len(self.matA)
        self.colB = Client.transpose(self,self.matB)
        self.ncolB = len(self.colB)
        #self.address = sock_add

    def transpose(self, mat):
        self.mat = mat
        lis = []
        tmat = []

        row = len(mat)
        col = len(mat[0])

        for i in range(col):
            for j in range(row):
                lis.append(mat[j][i])
            tmat.append(lis)
            lis = []
        return tmat

    def setmatrix(self, sock):

        a = sock.recv(1024)
        a = loads(a)

        print('ahdsalkjhd')

        x = 0
        rowC, C = [], []

        for i in range (0,self.nrowA):
            for j in range (0, self.ncolB):
                rowC.append(a[x])
                x += 1
            C.append(rowC)
            rowC = []

        print(C)


    def sendtasks(self):

        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect(self.dest)

        for i in range(self.nrowA):
            for j in range(self.ncolB):
                rxc = (self.matA[i],self.colB[j])
                tp = dumps(rxc)
                tcp.send(tp)
                time.sleep(0.01)

        tcp.send(dumps(''))

        Client.setmatrix(self,tcp)
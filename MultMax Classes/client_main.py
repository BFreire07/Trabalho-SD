from Client import *


def main(matA, matB):

    host = ('localhost',7035)
    a = Client(se,ae,host)
    a.sendtasks()

if __name__ == '__main__':

    se = [[2, 5, 9, 3, 8], [4, 3, 3, 2, 1], [1, 0, 9, 2, 0], [1, 5, 4, 5, 4]]
    ae = [[2, 8], [2, 3], [17, 3], [36, 44], [15, 114]]

    main(se, ae)

import socket, _thread
from BagOfTasks import *
from pickle import dumps, loads
from Worker import Worker

def conect(conn, addr):
    print('Conectado com:', addr)

    bag = BagOfTasks()
    mutex = threading.Lock()

    while True:
        msg  = conn.recv(1024)
        msg = loads(msg)
        if (msg == ''):
            break
        else:
            bag.insertBag(msg)

    tasks = []
    res = []

    bagsize = len(bot)

    for i in range (bagsize):
        a = bot.pop(0)
        thread = Worker(a, mutex)
        thread.start()
        tasks.append(thread)

    for thread in tasks:
        res.append(thread.join())

    conn.send(dumps(res))
    conn.close()
    _thread.exit()



def main():

    host = 'localhost'
    port  = 7035

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp.bind((host, port)   )
    tcp.listen(1)

    while True:
        conn, addr = tcp.accept()

        x = (conn, addr)

        _thread.start_new_thread(conect,x)


    print('FIM')
    print(bot)

if __name__ == '__main__':
    main()

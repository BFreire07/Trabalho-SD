import threading

class Worker(threading.Thread):

    def __init__(self, a, mutex):
        self.a = a
        self.mutex = mutex
        threading.Thread.__init__(self)


    def run(self):
        with self.mutex:
            a = self.a[0]
            b = self.a[1]
            self.soma = 0
            i = 0
            while (i<len(a)):
                self.soma += (a[i]*b[i])
                i += 1


    def join(self):
        threading.Thread.join(self)
        return  self.soma

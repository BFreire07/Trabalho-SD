import threading

class Worker(threading.Thread):

    def __init__(self, a, mutex):
        self.a = a
        self.mutex = mutex
        threading.Thread.__init__(self)
        self._return = None


    def run(self):

        with self.mutex:
            k = len(self.a[0])
            a = self.a[0]
            b = self.a[1]
            self.soma = 0
            for i in range (0, k):
                self.soma += (a[i]*b[i])


    def join(self):
        threading.Thread.join(self)
        return  self.soma
import rpyc
from rpyc.utils.server import ThreadedServer

i = 0
N = 1000000

class MyService(rpyc.Service):

    def exposed_f(self):
        print(42)
        return 42
    
    def g(self):
        print(43)
        return 43

if __name__ == "__main__":
    t = ThreadedServer(MyService, port=18861)
    t.start()

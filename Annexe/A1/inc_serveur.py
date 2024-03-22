import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Lock

i = 0
N = 1000000
lock = Lock()

class MyService(rpyc.Service):
    def exposed_inc(self):
        global i
        lock.acquire()
        i += N
        lock.release()
        print(f"N - i = {N-i}")

if __name__ == "__main__":
    t = ThreadedServer(MyService, port=18861)
    t.start()

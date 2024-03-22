import time
from random import randint
from Armoire5 import *
import threading

class simulation(threading.Thread):

    def __init__(self,pause ,duree):
        threading.Thread.__init__(self)
        self.pause=pause
        self.duree=duree

    def run(self):
        deb = time.time()
        fin = deb + self.duree
        a = Armoire5()

        while time.time() < fin:
            c = randint(0,6)
            s = randint(1,2)
            a.toggleCharge(c)
            a.togglesource(c)
            print(f"modification de la charge {c} mise sur source {s}")




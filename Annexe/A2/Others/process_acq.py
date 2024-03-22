import time
from random import randint
from Armoire5 import *
from threading import*
import threading

class acquisition(threading.Thread):

    def __init__(self,pause ,duree,liste):
        threading.Thread.__init__(self)
        self.pause=pause
        self.duree=duree
        self.liste=liste

    def run(self):
        L=self.liste
        deb = time.time()
        fin = deb + self.duree
        a = Armoire5()
        while time.time() < fin:
            time.pause=randint(0,9)
            l=a.readSecteur2()
            L.append(l)
            print(L)
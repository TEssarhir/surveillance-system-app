from Armoire5 import *
import time
from random import randint

def simulation(pause ,duree):
    deb = time.time()
    fin = deb + duree
    a = Armoire5()

    while time.time() < fin:
        c = randint(0,6)
        s = randint(1,2)
        a.toggleCharge(c)
        a.togglesource(c)
        print(f"modification de la charge {c} mise sur source {s}")
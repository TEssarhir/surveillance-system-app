import random
from threading import Semaphore, Thread, Condition


class Tampon():
    def __init__(self,limit):
        self.tampon = []
        self.limit=limit
        self.mutex=Semaphore(1)
        self.placelibre=Semaphore(self.limit)
        self.placeOccupee=Semaphore(0)
    def produire(self,val):
        self.placelibre.acquire()
        self.mutex.acquire()
        print("on produit",val)
        self.tampon.append(val)
        self.mutex.release()
        self.placeOccupee.release()
    def consommer(self):

        self.placeOccupee.acquire()
        self.mutex.acquire()
        res=self.tampon.pop(0)
        print("on consomme", res)
        self.mutex.release()
        self.placelibre.release()
        return res


class Producteur(Thread):
    def __init__(self,tampon : Tampon,nbfois):
        Thread.__init__(self)
        self.file=tampon
        self.nb=nbfois
    def run(self):
        for ignore in range(self.nb):
            val=random.randint(0,9)
            self.file.produire(val)
        print("fin producteur")



class Consommateur(Thread):
    def __init__(self, tampon: Tampon, nbfois):
        Thread.__init__(self)
        self.file = tampon
        self.nb = nbfois
    def run(self):
        for ignore in range(self.nb):
           val=self.file.consommer()

        print("fin consommateur")

def test(nbP,nbC,nbfoisP,nbfoisC):
    tampon=Tampon(4)
    for i in range(nbP):
        Producteur(tampon,nbfoisP).start()
    for i in range(nbC):
        Consommateur(tampon,nbfoisC).start()
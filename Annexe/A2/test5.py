from Armoire5 import *

def pprint(mesure):
    output="U={:.2f} I={:.2f} PA={:.2f} PR={:.2f}"
    return output.format(mesure[0],mesure[1],mesure[2],mesure[3])

def test(charge):

    a=Armoire5()
    a.resetAll()
    print("charge ",charge)
    a.setCharge(charge)
    s=a.readMesure(charge)
    print(pprint(s), "\nS1" ,pprint(a.readSecteur1()),"\nS2", pprint(a.readSecteur2()),"\n")
    a.setSource2(charge)
    s=a.readMesure(charge)
    print(pprint(s), "\nS1" ,pprint(a.readSecteur1()),"\nS2", pprint(a.readSecteur2()),"\n")
    a.unsetCharge(charge)
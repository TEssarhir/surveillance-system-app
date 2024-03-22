# -*- coding: utf-8 -*-
"""
Seule Test est à utiliser

@author: chevrier6
"""

from Armoire5 import *
#
# a=Armoire6()
# a.resetAll()
# i=0
# a.setCharge(i)
# s=a.readMesure(i)
# print(s)
#
# def chenillard():
#     a=Armoire6()
#     for i in range(a.nbCharge):
#         a.setCharge(i)
#         s=a.readMesure(i)
#         print(s)

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

#
# def chenillard2():
#     a=Armoire6()
#     a.resetAll()
#     for i in range(a.nbCharge):
#         print("charge ",i)
#         a.setCharge(i)
#         s=a.readMesure(i)
#         print(s, "S1" ,a.readSecteur1(),"S2", a.readSecteur2())
#         a.setSource2(i)
#         s=a.readMesure(i)
#         print(s, "S1" ,a.readSecteur1(),"S2", a.readSecteur2())
#         a.unsetCharge(i)
#
#
# def chenillard3():
#     a=Armoire6()
#     a.resetAll()
#     for charge in range(a.nbCharge):
#         print("charge ",charge)
#         a.setCharge(charge)
#         u,i,pa,pr=a.readMesure(charge)
#         u1,i1,pa1,pr1=a.readSecteur1()
#         u2,i2,pa2,pr2=a.readSecteur2()
#         print((u,i,pa,pr), "S1" ,a.readSecteur1(),"S2", a.readSecteur2())
#         print(u-u1,i-i1,pa-pa1,pr-pr1)
#         print(u-u2,i-i2,pa-pa2,pr-pr2)
#         a.setSource2(charge)
#         u,i,pa,pr=a.readMesure(charge)
#         u1,i1,pa1,pr1=a.readSecteur1()
#         u2,i2,pa2,pr2=a.readSecteur2()
#         print((u,i,pa,pr), "S1" ,a.readSecteur1(),"S2", a.readSecteur2())
#         print(u-u1,i-i1,pa-pa1,pr-pr1)
#         print(u-u2,i-i2,pa-pa2,pr-pr2)
#         a.unsetCharge(charge)
#
# def chenillard2b():
#     a=Armoire6()
#     a.resetAll()
#     for i in range(a.nbCharge):
#         print("charge ",i)
#         a.toggleCharge(i)
#         s=a.readMesure(i)
#         print(s, "S1" ,a.readSecteur1(),"S2", a.readSecteur2())
#         a.setSource2(i)
#         s=a.readMesure(i)
#         print(s, "S1" ,a.readSecteur1(),"S2", a.readSecteur2())
#         a.unsetCharge(i)

#chenillard2b()
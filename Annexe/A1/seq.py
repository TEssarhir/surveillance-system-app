import time
from random import shuffle
from acquisition import *
import numpy as np

def moyennes_mesures(mesures):
    moyennes = {}
    for mesure, t, n in mesures:
        print(f"Collecte de {n} valeurs de {mesure} toutes les ({t}s)...")
        valeurs = getMesure(mesure, t, n)
        moyenne = np.mean(valeurs)
        print(f"Moyenne de {mesure} est {moyenne:.2f}")


if __name__ == "__main__":
    shuffle(MESURES)
    print(MESURES)
    start_time = time.time()
    moyennes_mesures(MESURES)
    end_time = time.time()
    print(f"Temps de calcul: {end_time - start_time:.1f}s")
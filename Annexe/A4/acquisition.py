import numpy as np
import time
# Une liste de mesures. Chaque imesure est un couple
# (nom, temps d'acquisition en secondes, n valeurs).
MESURES = [
    ("U", 5,4),
    ("I", 5,4),
    ("PA", 6,4),
    ("PR", 6,4),
]


def getMesure(m,t,n):
    sigma = 0.1
    if m == 'U':
        mu = 5
    elif m == 'I':
        mu = 1
    elif m == 'PA':
        mu = 2
    elif m == 'PR':
        mu = 3
    time.sleep(t)
    valeurs = np.random.normal(mu, sigma, n)
    return valeurs
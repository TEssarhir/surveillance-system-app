import time
import rpyc
import numpy as np
from acquisition import *

def create_connection():
    return rpyc.connect("localhost", 18861)


def calcul_moyenne(id_, mesure, t, n):
    print(f"Moyenne de {mesure} est en préparation ({t}s)")
    valeurs = getMesure(mesure,t,n)
    moyenne = np.mean(valeurs)
    return f"Moyenne de {mesure} est {moyenne:.2f}"


def send_result(conn, task, result):
    conn.root.receive_result(task, result)


def ask_task(conn):
    task = conn.root.give_task()
    return task


def run(conn):
    #? `task` est un tuplet `(mesure, temps de préparation, nombre de valeurs)`.
    task = ask_task(conn)
    print(task)
    while task:
        id_, (mesure, t,n)  = task

        print(f"{mesure} à calculer reçue {id_}")
        prepared_moyenne = calcul_moyenne(id_, mesure, t,n)

        print(f"Moyenne de {mesure} prête envoyée {id_}")
        send_result(conn, task, prepared_moyenne)

        task = ask_task(conn)


if __name__ == "__main__":
    run(create_connection())

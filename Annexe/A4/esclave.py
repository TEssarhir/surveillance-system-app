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

def send_result(conn, task_number, measurement, result):
    conn.root.receive_result(task_number, measurement, result)

def ask_task(conn):
    task = conn.root.give_task()
    return task

def run(conn):
    #? `task` est un tuplet `(numéro de tâche, mesure, temps de préparation, nombre de valeurs)`.
    task = ask_task(conn)
    print(task)
    while task:
        task_number, (mesure, t, n) = task

        print(f"{mesure} à calculer reçue {task_number}")
        prepared_moyenne = calcul_moyenne(task_number, mesure, t, n)

        print(f"Moyenne de {mesure} prête envoyée {task_number}")
        send_result(conn, task_number, mesure, prepared_moyenne)

        task = ask_task(conn)

if __name__ == "__main__":
    run(create_connection())

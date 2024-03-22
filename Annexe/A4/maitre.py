from threading import Lock
from rpyc.utils.server import ThreadedServer
import rpyc
import time
from acquisition import MESURES
from bloc import Bloc
import utilitaires

tasks_to_do = [(i, mesure) for i, mesure in enumerate(MESURES)]
tasks_being_done = []
lock = Lock()
start_time = None
l = len(tasks_to_do)
difficulty = 1  # Initialisation de la difficulté

class MasterService(rpyc.Service):

    def exposed_give_task(self):
        global start_time
        if len(tasks_to_do) == 0:
            return None
        else:
            lock.acquire()
            start_time = time.time() if not start_time else start_time  # Afin d'éviter de réinitialiser le temps à chaque tâche de l'esclave
            task = tasks_to_do.pop(0)  # Pour enlever la tache de la liste
            lock.release()
            return task
    
    def exposed_receive_result(self, task_number, measurement, result):
        
        print(f"{result} received")
        tasks_being_done.append((task_number, measurement, result))

        if len(tasks_being_done) == l:
            print(f"Tous les mesures sont éffectués, temps total : {time.time() - start_time}")

            # Créer la chaîne de blocs
            blockchain = []
            previous_hash = "0"
            for task_number, measurement, result in tasks_being_done:
                data = {"task_number": task_number, "measurement": measurement, "result": result}
                bloc = Bloc(data, previous_hash)
                bloc.mineBlock(difficulty)
                blockchain.append(bloc)
                previous_hash = bloc.hash

            # Afficher la liste des blocs
            print("\nListe des blocs:")
            for bloc in blockchain:
                print(f"Data : {bloc.data}\n")
                print(f"Hash : {bloc.hash}\n")

            # Vérifier la validité de la chaîne
            if utilitaires.isChaineValid(blockchain):
                print("La chaîne est valide.")
            else:
                print("La chaîne n'est pas valide.")

            tasks_being_done.clear()

#* Le script esclave est éxecutable depuis le repertoire relative '../A1/esclave.py'
if __name__ == "__main__":
    server = ThreadedServer(MasterService, port=18861)
    server.start()
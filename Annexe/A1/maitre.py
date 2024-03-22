from threading import Lock
from rpyc.utils.server import ThreadedServer
import rpyc
import time
from acquisition import MESURES

tasks_to_do = [(i, mesure) for i, mesure in enumerate(MESURES)]
tasks_being_done = []
lock = Lock()
start_time = None
l = len(tasks_to_do)

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
    
    def exposed_receive_result(self, task, result):
        print(f"{result} received")
        tasks_being_done.append(task)
        if len(tasks_being_done) == l:
            print(f"Tous les mesures sont éffectués, temps total : {time.time() - start_time}")
            

if __name__ == "__main__":
    server = ThreadedServer(MasterService, port=18861)
    server.start()

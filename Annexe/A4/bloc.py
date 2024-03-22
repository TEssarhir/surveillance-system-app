import hashlib
import time

class Bloc:


    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.timeStamp = time.time()
        self.nonce = 0
        self.hash = self.calculateHash()


    def calculateHash(self):
        "Calcul de la valeur de hashage en utilisant l'algorithme SHA256"

        sha = hashlib.sha256()
        hash_str = (str(self.previousHash) + str(self.timeStamp) + str(self.data) + str(self.nonce)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    

    def mineBlock(self, difficulty):
        "Algorithme de minage qui prend en argument le paramètre `difficulty` et renvoie la valeur de hashage du bloc"

        target = "0" * difficulty
        while self.hash is None or self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculateHash()
        print(f"Bloc miné avec succès.\nHash :{self.hash}")
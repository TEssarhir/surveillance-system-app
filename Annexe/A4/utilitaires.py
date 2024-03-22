import hashlib

def applySha256(input):

    sha = hashlib.sha256()
    sha.update(input.encode('utf-8'))
    return sha.hexdigest()

def isChaineValid(blockchain):

    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        
        if current_block.hash != current_block.calculateHash(): # Vérification du hash actuel avec la valeur calculée
            return False
        
        if current_block.previousHash != previous_block.hash: # Vérification du previousHash
            return False
        
    return True
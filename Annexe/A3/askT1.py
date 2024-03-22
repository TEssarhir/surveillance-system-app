
#exemple de requete
import requests

requetes =["http://127.0.0.1:5000/",
"http://127.0.0.1:5000/bonjour",
"http://127.0.0.1:5000/bonjour?nom=vincent"]


for txt in requetes:
    r = requests.get(txt)
    print(r.text)


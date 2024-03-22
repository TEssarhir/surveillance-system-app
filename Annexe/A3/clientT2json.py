import requests
import time

test2="http://127.0.0.1:5000/service1j"
adresse=test2

for i in range(10):
    time.sleep(1)
    r = requests.get(adresse)
    rep=  r.json()

    print(r.text, rep['text'],rep['hour']+rep['min'],rep.get('inconnu'))
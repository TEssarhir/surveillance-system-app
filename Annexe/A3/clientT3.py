import requests


test2="http://127.0.0.1:5000/service0?a=4&c=34"
adresse=test2


r = requests.get(adresse)
print(r.text)
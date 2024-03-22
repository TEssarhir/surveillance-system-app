
from flask import Flask
from datetime import datetime

compteur=0
app = Flask(__name__)  # notre appli

@app.route('/service1') #  service (service1) et la fonction associé
def dire_coucou():
    global compteur
    compteur+=1
    myTime =datetime.today()

    txt=str(myTime.hour)+"h "+str(myTime.minute)+"min "+str( myTime.second)+"s"
    return 'appel n° '+ str(compteur)+"  "+txt
#http://127.0.0.1:5000/service1  # appel
app.run(debug=True)
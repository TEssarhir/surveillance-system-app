
from flask import Flask
from datetime import datetime

app = Flask(__name__)  # notre appli

@app.route('/service1') #  service (service1) et la fonction associé
def dire_coucou():
    myTime =datetime.today()
    txt=str(myTime.hour)+"h "+str(myTime.minute)+"min "+str( myTime.second)+"s"
    return 'Coucou ! il est '+ txt
#http://127.0.0.1:5000/service1  # appel
app.run(debug=True)
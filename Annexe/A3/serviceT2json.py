
from flask import Flask,jsonify

from datetime import datetime

app = Flask(__name__)

@app.route('/service1j')
def dire_coucou():
    myTime =datetime.today()
    return jsonify(text='Coucou ! il est ',hour=myTime.hour,min=myTime.minute,second=myTime.second)
#http://127.0.0.1:5000/service1j
app.run(debug=True)
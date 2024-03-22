
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello ! serveur de test"


@app.route('/bonjour')
def dire_bonjour():
    args = request.args
    nom = args.get('nom')
    if nom==None:
        nom='inconnu'
    return 'bonjour '+nom


#exemple de requete
#http://127.0.0.1:5000/
#http://127.0.0.1:5000/bonjour
#http://127.0.0.1:5000/bonjour?nom=vincent
app.run(debug=True)

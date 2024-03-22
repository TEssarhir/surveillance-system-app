
from flask import Flask, request  # on importe le necessaire

app = Flask(__name__) # notre appli

@app.route('/service0')  # l'adresse sera service0 sur le serveur, le code en dessous sera la fonction appelée
def requete():
    args = request.args
    print ("print info",args.values(),args.keys(),args.items()) # For debugging
    rep=""
    for k,v in args.items():
        print (k,v)
        rep+="("+k+","+v+")"
    return rep
# http://127.0.0.1:5000/service0?a=4&c=34  # exemple de texte à saisir dans un navigateur
#changer l'adresse avec celle fournie dans le shell
app.run(debug=True,host='0.0.0.0')
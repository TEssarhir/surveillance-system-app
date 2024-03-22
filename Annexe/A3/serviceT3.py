import json

from flask import Flask, request, jsonify  # on importe le necessaire

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
# http://127.0.0.1:5000/exercise0  # exemple de texte à saisir dans un navigateur si host pas précisé
# sinon voir l'adresse indiquée


@app.route('/exemple3')
def exemple3():
    data=request.args
    print( data['valeur'])
# Modifiez pour renvoyer le nombre de minute
    return "plouf"
#http://127.0.0.1:5000//exemple3?valeur={"hour": 8, "min": 53, "second": 17, "text": "Coucou ! il est "}



@app.route('/exemple4')  #
def mini():
    args = request.args
    liste=args['liste']
    val=json.loads(liste)
    mini=min(val)
    return jsonify(min=mini)
#http://127.0.0.1:5000//exemple4?liste=[3,75,-9]

@app.route('/exemple5')  #
def somme():
    args = request.args
    a=int(args['a'])
    b=int(args['b'])

    return jsonify(somme=a+b)
#http://127.0.0.1:5000//exemple5?a=12&b=2

app.run(debug=True)
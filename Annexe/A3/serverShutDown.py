
from flask import Flask, request  # on importe le necessaire

app = Flask(__name__) # notre appli

# from http://web.archive.org/web/20190706125149/http://flask.pocoo.org/snippets/67
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route('/service0')  # un service peu importe lequele
def requete():
    args = request.args
    print ("print info",args.values(),args.keys(),args.items()) # For debugging
    rep=""
    for k,v in args.items():
        print (k,v)
        rep+="("+k+","+v+")"
    return rep
# http://127.0.0.1:5000/service0?a=4&c=34  # exemple de texte à saisir dans un navigateur
app.run(debug=True)
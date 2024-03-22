
from flask import Flask, jsonify, request, url_for

app = Flask(__name__)

# define some data

data = [
    {
        'id': 1,
        'name': 'motor async',
        'description': 'Ma bioutifoul motor with plein de puissance',
        'done': False
    },
    {
        'id': 2,
        'title': 'PV pannel',
        'description': 'provide you nice power',
        'power': 1000
    }
]



@app.route('/data', methods=['GET'])
def get_tasks():
    return jsonify({'data': data})

@app.route('/dataSole', methods=['GET'])
def requete():
    args = request.args
    print ("print info",args) # For debugging
    return "yes"

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    a =request.args.get('a')

    return '''<h1>The language value is: {} et a est {}</h1>'''.format(language,a)


@app.route('/qa-example2',methods=['GET','POST'])
def qa_example():
    if request.method == 'POST':
       return "c'est un post"
    else:
        language = request.args.get('language')
        a = request.args.get('a')
        return '''<h1>The language value is: {} et a est {}</h1>'''.format(language, a)


@app.route('/')
def index():
    return "this is the base page for my bioutifoul app !\p" + \
           "<p>test page racine. connexion sur http://127.0.0.1:5000/ <a href=\"http://127.0.0.1:5000\">Lelien attention ça boucle</a>" + \
           "\n url pour requete"+str(url_for('requete'))


app.run(debug=True)
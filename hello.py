from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hola Mundo</h1>'

@app.route('/person/<a_name>')
def person(a_name):
    return '<h1>Hola, %s</h1>' % a_name

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return '<h1>Hola, %s </h1><h3>Contraseña=%s</h3>' % (username, password)

@app.route('/person/<a_name>/edad/<int:age>')
def theage(a_name,age):
    rest = 100 - age
    return '<h1>Hola, %s </h1><h3>En %d años tendras 100 años</h3>' % (a_name, rest)

@app.route('/advices')
def ideas():
    data = {
        'status' : 'OK',
        'advice1' : 'Primer aviso',
        'advice2' : 'Segundo aviso',
        'advice3' : 'Tercer aviso'
    }
    return jsonify(data);

if __name__ == '__main__':
    app.run(port=5003,debug=True)



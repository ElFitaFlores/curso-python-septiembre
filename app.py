from flask import Flask, request, redirect, Blueprint

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello world"

@app.route('/')
def index():
    return 'Welcome'

@app.route('/healthcheck')
def health_check():
    return 'Service healthy'

@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f"Hola {nombre}"


# int, string, float, path, uuid (e4088334-27e7-4691-a899-789fb885da56)
@app.route('/edad/<int:numero>')
def edad(numero):
    return f"Tienes {numero} años"

@app.route('/helado', methods=['POST', 'PUT'])
def helado():
    return 'Toma tu helado'

@app.post('/animal')
def animal():
    return 'Bienvenido al zoo'

@app.post('/llaves')
def llaves_post():
    return "Estas guardando llaves"

@app.get('/llaves')
def llaves_get():
    return "Estas consultando las llaves"

@app.post('/registro')
def registro():
    return {
        'method': request.method,
        'body': request.form,
        'date': request.date
    }

@app.errorhandler(404)
def not_found(error):
    return 'Endpoint not found', 404

@app.route('/redirect')
def redirect_endpoint():
    return redirect('/')

bp_user = Blueprint('user', __name__, url_prefix='/users')

@bp_user.route('/<id>')
def show_user(id):
    return {
        'nombre': 'Fulano',
        'id': id
    }

app.register_blueprint(bp_user)
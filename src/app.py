from flask import Flask
from decouple import config
from modelo.Estudiantes import ModeloEstudiante
from config import config

app = Flask(__name__)

# RUTA PARA PETICION GET

@app.route("/")
def hello_world():
    return  " hola mundo "

#mostrar todos los estudiantes
@app.route("/estudiantes", methods=['GET'])
def listar_estudiantes():
    resul=ModeloEstudiante.listar_Estudiante()
    return resul

#buscar solo un estudiante
@app.route("/estudiantes/:<codigo>", methods=['GET'])
def lista_estudiante(codigo):
    resul=ModeloEstudiante.lista_Estudiante(codigo)
    return resul

#registrar estudiante
@app.route("/estudiantes",methods=['POST'])
def guardar_estudiante():
    resul=ModeloEstudiante.registrar_estudiante()
    return resul


#actualizar estudiante
@app.route("/estudiantes/:<codigo>",methods=['PUT'])
def actualizxar_estudiante(codigo):
    resul=ModeloEstudiante.actualizar_estudiante(codigo)
    return resul


#eliminar estudiante
@app.route("/estudiantes/:<codigo>",methods=['DELETE'])
def elimineycion_estudiante(codigo):
    resul=ModeloEstudiante.eliminar_estuy(codigo)
    return resul

def pag_noencontrada(error):
    return "<h1>Página no Encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pag_noencontrada)
    app.run(host='0.0.0.0')

  
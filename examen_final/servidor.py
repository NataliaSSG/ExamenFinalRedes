from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import base64 # Para decodificar la imagen

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(mensaje='Wii')

@app.route('/desencriptar-imagen', methods=['POST'])
def desencriptar_imagen():
    data = request.get_json()
    imagen_encriptada = base64.b64decode(data['mensaje'])
    
    # Checa si existe la llave en el header
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify(error='No se envio la llave'), 401
    
    # Obtiene la llave del header
    key = request.headers.get('Authorization').split()[1].encode()
    cipher_suite = Fernet(key)
    
    # Desencripta la imagen
    imagen_desencriptada = cipher_suite.decrypt(imagen_encriptada)
    
    # Guarda la imagen desencriptada
    with open('imagen_desencriptada.png', 'wb') as f:
        f.write(imagen_desencriptada)
    return jsonify(mensaje='Imagen desencriptada exitosamente'), 200


# SERVIDOR EN PUERTO 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, jsonify
from cryptography.fernet import Fernet
import base64 # Para decodificar la imagen

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(mensaje='Wii')

@app.route('/subir-imagen', methods=['POST'])
def encriptar_imagen():
    # Se lee la imagen ya encontrada en el directorio
    with open('gato.png', 'rb') as f:
        image = f.read()
        
    # Genera una llave y encripta la imagen
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_image = cipher_suite.encrypt(image)
    
    # Regresa la imagen encriptada y la llave en json
    return jsonify({"mensaje": base64.b64encode(encrypted_image).decode(), "llave": key.decode()})


# CLIENTE EN PUERTO 5001
if __name__ == '__main__':
    app.run(debug=True, port=5001)
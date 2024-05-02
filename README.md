# ExamenFinalRedes

Librerías necesarias de Python:  
- flask  
- cryptography  
Comandos: pip install flask cryptography  

Pasos para correr el programa:
1. Correr ambos archivos .py, ya sea en diferentes terminales en VSCode simplemente corriendo el código, o ejecutando:
   - python3 cliente.py  
   - python3 servidor.py
    
2. Desde Postman, hacer la petición desde el lado del cliente:
   - http://127.0.0.1:5001/subir-imagen
   Esta petición es para encriptar la imagen. Esta imagen ya se encuentra en el directorio. La respuesta será una llave y la imagen encriptada.

3. Desde Postman, hacer la petición:
   - http://127.0.0.1:5000/desencriptar-imagen
   Para que la petición sea exitosa, hay que ingresar la llave obtenida en el punto anterior como Bearer Token. En el cuerpo, hay que ingresar el mensaje obtenido en el punto anterior. Es decir, el JSON copiado sin la llave.

4. Al realizar esto, se debe ver la imagen desencriptada en el directorio. 

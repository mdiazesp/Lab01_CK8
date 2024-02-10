#!/bin/python

from flask import Flask, request

app = Flask(__name__)

# Metodos API REST

@app.route('/')
def saludo():
    return 'Hola desde mi servicio!'

# Lanzamiento de Servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

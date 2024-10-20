from flask import Flask, request, jsonify
import os
import json
from dotenv import load_dotenv
from epaycosdk.epayco import Epayco

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Inicializa ePayco con las claves de la cuenta
epayco = Epayco({
    'apiKey': os.getenv('EPAYCO_PUBLIC_KEY'),
    'privateKey': os.getenv('EPAYCO_PRIVATE_KEY'),
    'lenguaje': 'ES',
    'test': os.getenv('EPAYCO_TEST') == 'true' # Se define si es modo de prueba o producción
})

# Método para crear el token de la tarjeta
def create_token(data):
    try:
        card_info = {
            'card[number]': data['card_number'],
            'card[exp_year]': data['exp_year'],
            'card[exp_month]': data['exp_month'],
            'card[cvc]': data['cvc'],
            'hasCvv': True
        }
        token = epayco.token.create(card_info)
        return token
    except Exception as e:
        return {'error': str(e)}

# Método para crear el cliente
def create_customer(token, data):
    customer_info = {
        'name': data['name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'phone': data['phone'],
        'default': True
    }
    try:
        customer = epayco.customer.create(customer_info)
        return customer
    except Exception as e:
        return {'error': str(e)}
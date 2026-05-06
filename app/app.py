import os
from flask import Flask, jsonify

app = Flask(__name__)

# Configuração da versão do sistema através de variável de ambiente ou estática

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "Blue-Environment")

@app.route('/')
def home():
    return jsonify({
        "status": "Aeronave em voo estabilizado",
        "ambiente": APP_ENV,
        "versao": APP_VERSION
    })

@app.route('/telemetria')
def telemetria():
    # Simulando um bug crítico introduzido na versão 2.1.0
    if APP_VERSION == "2.1.0":
        return jsonify({
            "erro": "CRITICAL_SYSTEM_FAIL: Pane nos motores simulada!",
            "status": "EJECT_IMMEDIATELY"
        }), 500
        
    return jsonify({
        "sensores": "OK",
        "combustivel": "92%",
        "versao": APP_VERSION
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

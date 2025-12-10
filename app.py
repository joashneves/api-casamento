import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Import Blueprints
from routes.rsvp import rsvp_blueprint
from routes.auth import auth_blueprint
from routes.gift import gift_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/rsvp_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models.rsvp import db
from models.gift import Gift # Import Gift model
db.init_app(app)

# Register Blueprints
app.register_blueprint(rsvp_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(gift_blueprint)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-control-allow-headers'] = 'Content-Type, Authorization'
    return response

@app.route('/')
def hello_world():
    return jsonify({"message": "Olá, mundo!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Cria as tabelas se não existirem (apenas para desenvolvimento)
    app.run(host='0.0.0.0', debug=True, port=5000)
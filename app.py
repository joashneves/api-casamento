import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/rsvp_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models.rsvp import db, RSVP
db.init_app(app)

@app.route('/')
def hello_world():
    return jsonify({"message": "Olá, mundo!"})

@app.route('/api/rsvp', methods=['POST'])
def handle_rsvp():
    data = request.get_json()

    if not data or 'name' not in data or 'attending' not in data:
        return jsonify({'error': 'Dados inválidos: nome e presença são obrigatórios.'}), 400

    name = data.get('name')
    attending = data.get('attending')
    message = data.get('message', '')

    new_rsvp = RSVP(name=name, attending=attending, message=message)
    db.session.add(new_rsvp)
    db.session.commit()

    return jsonify({'message': 'Confirmação recebida com sucesso!', 'id': new_rsvp.id}), 201

@app.route('/api/rsvps', methods=['GET'])
def get_all_rsvps():
    rsvps = RSVP.query.all()
    return jsonify([rsvp.to_dict() for rsvp in rsvps]), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Cria as tabelas se não existirem (apenas para desenvolvimento)
    app.run(host='0.0.0.0', debug=True, port=5000)
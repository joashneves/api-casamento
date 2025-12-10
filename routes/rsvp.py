from flask import Blueprint, request, jsonify
from models.rsvp import db, RSVP
from utils.auth import admin_required

rsvp_blueprint = Blueprint('rsvp', __name__)

@rsvp_blueprint.route('/api/rsvp', methods=['POST'])
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


@rsvp_blueprint.route('/api/rsvps', methods=['GET'])
def get_rsvps():
    rsvps = RSVP.query.all()
    return jsonify([rsvp.to_dict() for rsvp in rsvps])

@rsvp_blueprint.route('/api/rsvps/<int:id>', methods=['GET'])
@admin_required
def get_rsvp(id):
    rsvp = RSVP.query.get_or_404(id)
    return jsonify(rsvp.to_dict())

@rsvp_blueprint.route('/api/rsvps/<int:id>', methods=['PUT'])
@admin_required
def update_rsvp(id):
    rsvp = RSVP.query.get_or_404(id)
    data = request.get_json()
    rsvp.name = data.get('name', rsvp.name)
    rsvp.attending = data.get('attending', rsvp.attending)
    rsvp.message = data.get('message', rsvp.message)
    db.session.commit()
    return jsonify(rsvp.to_dict())

@rsvp_blueprint.route('/api/rsvps/<int:id>', methods=['DELETE'])
@admin_required
def delete_rsvp(id):
    rsvp = RSVP.query.get_or_404(id)
    db.session.delete(rsvp)
    db.session.commit()
    return '', 204

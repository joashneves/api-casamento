from flask import Blueprint, request, jsonify
from models.rsvp import db
from models.gift import Gift
from utils.auth import admin_required

gift_blueprint = Blueprint('gift', __name__)

# Admin route to add a new gift
@gift_blueprint.route('/api/gifts', methods=['POST'])
@admin_required
def add_gift():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'message': 'Gift name is required'}), 400

    new_gift = Gift(
        name=data['name'],
        price=data.get('price'),
        link=data.get('link'),
        image_url=data.get('image_url') # New field
    )
    db.session.add(new_gift)
    db.session.commit()
    return jsonify(new_gift.to_dict()), 201

# Public route to get all gifts
@gift_blueprint.route('/api/gifts', methods=['GET'])
def get_gifts():
    gifts = Gift.query.order_by(Gift.is_gifted, Gift.price).all()
    return jsonify([gift.to_dict() for gift in gifts])

# Admin route to update a gift
@gift_blueprint.route('/api/gifts/<int:id>', methods=['PUT'])
@admin_required
def update_gift(id):
    gift = Gift.query.get_or_404(id)
    data = request.get_json()
    
    gift.name = data.get('name', gift.name)
    gift.price = data.get('price', gift.price)
    gift.link = data.get('link', gift.link)
    gift.image_url = data.get('image_url', gift.image_url) # New field
    gift.is_gifted = data.get('is_gifted', gift.is_gifted)
    gift.donor_name = data.get('donor_name', gift.donor_name)

    db.session.commit()
    return jsonify(gift.to_dict())

# Admin route to delete a gift
@gift_blueprint.route('/api/gifts/<int:id>', methods=['DELETE'])
@admin_required
def delete_gift(id):
    gift = Gift.query.get_or_404(id)
    db.session.delete(gift)
    db.session.commit()
    return '', 204

# Public route for a user to claim a gift
@gift_blueprint.route('/api/gifts/<int:id>/claim', methods=['POST'])
def claim_gift(id):
    gift = Gift.query.get_or_404(id)
    if gift.is_gifted:
        return jsonify({'message': 'This gift has already been claimed'}), 400

    data = request.get_json()
    if not data or not data.get('donor_name'):
        return jsonify({'message': 'Donor name is required'}), 400
        
    gift.is_gifted = True
    gift.donor_name = data['donor_name']
    db.session.commit()
    
    return jsonify(gift.to_dict())

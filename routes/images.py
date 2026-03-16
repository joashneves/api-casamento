import os
from flask import Blueprint, jsonify, send_from_directory

images_blueprint = Blueprint('images', __name__)

# Caminho absoluto para a pasta de imagens (na raiz do projeto)
IMAGES_FOLDER = os.path.join(os.getcwd(), 'imagensDeCasamento')

@images_blueprint.route('/api/images', methods=['GET'])
def list_images():
    try:
        if not os.path.exists(IMAGES_FOLDER):
            return jsonify({"error": "Pasta de imagens não encontrada"}), 404
            
        images = os.listdir(IMAGES_FOLDER)
        # Filtra apenas arquivos de imagem comuns
        image_extensions = ('.webp', '.jpg', '.jpeg', '.png', '.gif')
        images = [img for img in images if img.lower().endswith(image_extensions)]
        
        return jsonify(images)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@images_blueprint.route('/api/images/<path:filename>', methods=['GET'])
def download_image(filename):
    try:
        return send_from_directory(IMAGES_FOLDER, filename)
    except Exception as e:
        return jsonify({"error": "Imagem não encontrada"}), 404

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # Permitir CORS para todas as rotas

# Diretório base das imagens
IMAGES_DIR = 'portfolio_images'

@app.route('/api/portfolio-images')
def get_portfolio_images():
    """Retorna todas as imagens organizadas por categoria"""
    try:
        images_data = {
            'small': [],
            'medium': [],
            'large': []
        }
        
        # Mapeamento de pastas para categorias
        folder_mapping = {
            'carros_passeio': 'small',
            'veículos_comerciais': 'medium',
            'caminhoes_onibus': 'large'
        }
        
        # Verificar se o diretório de imagens existe
        if not os.path.exists(IMAGES_DIR):
            return jsonify({'error': 'Diretório de imagens não encontrado'}), 404
        
        # Listar imagens de cada pasta
        for folder, category in folder_mapping.items():
            folder_path = os.path.join(IMAGES_DIR, folder)
            if os.path.exists(folder_path):
                # Listar apenas arquivos de imagem
                image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
                files = os.listdir(folder_path)
                
                for file in files:
                    if any(file.lower().endswith(ext) for ext in image_extensions):
                        images_data[category].append({
                            'filename': file,
                            'src': f'portfolio_images/{folder}/{file}',
                            'alt': f'Trabalho profissional - {get_category_name(category)}'
                        })
        
        return jsonify(images_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_category_name(category):
    """Converte categoria para nome em português"""
    names = {
        'small': 'Carros de Passeio',
        'medium': 'Veículos Comerciais', 
        'large': 'Caminhões e Ônibus'
    }
    return names.get(category, category)

@app.route('/portfolio_images/<path:filename>')
def serve_image(filename):
    """Serve imagens estáticas"""
    return send_from_directory(IMAGES_DIR, filename)

@app.route('/')
def serve_index():
    """Serve o arquivo index.html"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve arquivos estáticos"""
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


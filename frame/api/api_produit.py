
from flask import request, Blueprint,jsonify
from frame import db
from ..models.produit import produits

api_produits = Blueprint('api_produits', __name__)


@api_produits.route('/api/produits')
def get_produits():
	return jsonify([
		{
			'id': produit.id, 'titre': produit.titre, 'description': produit.description,
			'prix': produit.prix,'color': produit.color
			} for produit in produits.query.all()
	])
		
@api_produits.route('/api/produit/<id>/')
def get_produit(id):
	print(id)
	produit = produits.query.filter_by(id=id).first_or_404()
	return {
		'id': produit.id, 'titre': produit.titre, 'description': produit.description,
			'prix': produit.prix,'color': produit.color
		}

@api_produits.route('/api/produit/add', methods=['POST'])
def create_produit():
	data = request.get_json()
	if not 'titre' in data or not 'description' in data:
		return jsonify({
			'error': 'Bad Request',
			'message': 'Titre or description not given'
		}), 400
	if len(data['titre']) < 4 or len(data['description']) < 4:
		return jsonify({
			'error': 'Bad Request',
			'message': 'Titre and description must be contain minimum of 4 letters'
		}), 400
	entry = produits(
			titre=data['titre'], 
			description=data['description'],
			prix=data['prix'],
			color=data['color']
		)
	db.session.add(entry)
	db.session.commit()
	return {
		'id': entry.id, 'titre': entry.titre, 'description': entry.description,
			'prix': entry.prix,'color': entry.color
	}, 201

@api_produits.route('/api/produit/update/<id>', methods=['PUT'])
def update_produit(id):
	data = request.get_json()
	if 'titre' not in data:
		return {
			'error': 'Bad Request',
			'message': 'titre field needs to be present'
		}, 400
	produit = produits.query.filter_by(id=id).first_or_404()
	produit.titre=data['titre']
	produit.description=data['description']
	produit.prix=data['prix']
	produit.color=data['color']

	
	db.session.commit()
	return jsonify({
		'id': produit.id, 'titre': produit.titre, 'description': produit.description,
			'prix': produit.prix,'color': produit.color
		})

@api_produits.route('/api/produit/delete/<id>', methods=['DELETE'] )
def delete_produit(id):
	produit = produits.query.filter_by(id=id).first_or_404()
	db.session.delete(produit)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}

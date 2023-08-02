
from flask import request, Blueprint,jsonify
from frame import db
from ..models.commande import commandes

api_commandes = Blueprint('api_commandes', __name__)


@api_commandes.route('/api/commandes')
def get_commandes():
	return jsonify([
		{
			'id': commande.id, 'nom': commande.tinomtre, 'reference': commande.reference
			
			} for commande in commandes.query.all()
	])
		
@api_commandes.route('/api/commande/<id>/')
def get_commande(id):
	print(id)
	commande = commandes.query.filter_by(id=id).first_or_404()
	return {
		'id': commande.id, 'nom': commande.nom, 'reference': commande.reference
			
		}

@api_commandes.route('/api/commande/add', methods=['POST'])
def create_commande():
	data = request.get_json()
	if not 'nom' in data or not 'reference' in data:
		return jsonify({
			'error': 'Bad Request',
			'message': 'nom or reference not given'
		}), 400
	if len(data['nom']) < 4 or len(data['reference']) < 4:
		return jsonify({
			'error': 'Bad Request',
			'message': 'nom and reference must be contain minimum of 4 letters'
		}), 400
	entry = commandes(
			nnom=data['nom'], 
			reference=data['reference']
		
		)
	db.session.add(entry)
	db.session.commit()
	return {
		'id': entry.id, 'nom': entry.nom, 'reference': entry.reference
			
	}, 201

@api_commandes.route('/api/commande/update/<id>', methods=['PUT'])
def update_commande(id):
	data = request.get_json()
	if 'nom' not in data:
		return {
			'error': 'Bad Request',
			'message': 'nom field needs to be present'
		}, 400
	commande = commandes.query.filter_by(id=id).first_or_404()
	commande.nom=data['nom']
	commande.reference=data['reference']
	db.session.commit()
	return jsonify({
		'id': commande.id, 'nom': commande.nom, 'reference': commande.reference
			
		})

@api_commandes.route('/api/commande/delete/<id>', methods=['DELETE'] )
def delete_commande(id):
	commande = commandes.query.filter_by(id=id).first_or_404()
	db.session.delete(commande)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}

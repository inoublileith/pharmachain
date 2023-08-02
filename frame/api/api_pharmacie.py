
from flask import request, Blueprint,jsonify
from frame import db
from ..models.pharmacie import pharmacies

api_pharmacies = Blueprint('api_pharmacies', __name__)


@api_pharmacies.route('/api/pharmacies')
def get_pharmacies():
	return jsonify([
		{
			'id': pharmacie.id, 'nom': pharmacie.nom, 'gouvernorat': pharmacie.gouvernorat,
			'ville': pharmacie.ville
			} for pharmacie in pharmacies.query.all()
	])
		
@api_pharmacies.route('/api/pharmacie/<id>/')
def get_pharmacie(id):
	print(id)
	pharmacie = pharmacies.query.filter_by(id=id).first_or_404()
	return {
		'id': pharmacie.id, 'nom': pharmacie.nom, 'gouvernorat': pharmacie.gouvernorat,
			'ville': pharmacie.ville
		}

@api_pharmacies.route('/api/pharmacie/add', methods=['POST'])
def create_pharmacie():
	data = request.get_json()
	if not 'nom' in data or not 'gouvernorat' in data:
		return jsonify({
			'error': 'Bad Request',
			'message': 'nom or gouvernorat not given'
		}), 400
	if len(data['nom']) < 4 or len(data['gouvernorat']) < 4:
		return jsonify({
			'error': 'Bad Request',
			'message': 'nom and gouvernorat must be contain minimum of 4 letters'
		}), 400
	entry = pharmacies(
			nom=data['nom'], 
			gouvernorat=data['gouvernorat'],
			ville=data['ville']
		)
	db.session.add(entry)
	db.session.commit()
	return {
		'id': entry.id, 'nom': entry.nom, 'gouvernorat': entry.gouvernorat,
			'ville': entry.ville
	}, 201

@api_pharmacies.route('/api/pharmacie/update/<id>', methods=['PUT'])
def update_pharmacie(id):
	data = request.get_json()
	if 'nom' not in data:
		return {
			'error': 'Bad Request',
			'message': 'nom field needs to be present'
		}, 400
	pharmacie = pharmacies.query.filter_by(id=id).first_or_404()
	pharmacie.nom=data['nom']
	pharmacie.gouvernorat=data['gouvernorat']
	pharmacie.ville=data['ville']
	

	
	db.session.commit()
	return jsonify({
		'id': pharmacie.id, 'nom': pharmacie.nom, 'gouvernorat': pharmacie.gouvernorat,
			'ville': pharmacie.ville
		})

@api_pharmacies.route('/api/pharmacie/delete/<id>', methods=['DELETE'] )
def delete_pharmacie(id):
	pharmacie = pharmacies.query.filter_by(id=id).first_or_404()
	db.session.delete(pharmacie)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}

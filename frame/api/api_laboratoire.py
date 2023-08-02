
from flask import request, Blueprint,jsonify
from frame import db
from ..models.laboratoire import laboratoires

api_laboratoires = Blueprint('api_laboratoires', __name__)


@api_laboratoires.route('/api/laboratoires')
def get_laboratoires():
	return jsonify([
		{
			'id': laboratoire.id, 'nom': laboratoire.nom, 'gouvernorat': laboratoire.gouvernorat,
			'ville': laboratoire.ville
			} for laboratoire in laboratoires.query.all()
	])
		
@api_laboratoires.route('/api/laboratoire/<id>/')
def get_laboratoire(id):
	print(id)
	laboratoire = laboratoires.query.filter_by(id=id).first_or_404()
	return {
		'id': laboratoire.id, 'nom': laboratoire.nom, 'gouvernorat': laboratoire.gouvernorat,
			'ville': laboratoire.ville
		}

@api_laboratoires.route('/api/laboratoire/add', methods=['POST'])
def create_laboratoire():
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
	entry = laboratoires(
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

@api_laboratoires.route('/api/laboratoire/update/<id>', methods=['PUT'])
def update_laboratoire(id):
	data = request.get_json()
	if 'nom' not in data:
		return {
			'error': 'Bad Request',
			'message': 'nom field needs to be present'
		}, 400
	laboratoire = laboratoires.query.filter_by(id=id).first_or_404()
	laboratoire.nom=data['nom']
	laboratoire.gouvernorat=data['gouvernorat']
	laboratoire.ville=data['ville']
	

	
	db.session.commit()
	return jsonify({
		'id': laboratoire.id, 'nom': laboratoire.nom, 'gouvernorat': laboratoire.gouvernorat,
			'ville': laboratoire.ville
		})

@api_laboratoires.route('/api/laboratoire/delete/<id>', methods=['DELETE'] )
def delete_laboratoire(id):
	laboratoire = laboratoires.query.filter_by(id=id).first_or_404()
	db.session.delete(laboratoire)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}

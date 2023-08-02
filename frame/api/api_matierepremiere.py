
from flask import request, Blueprint,jsonify
from frame import db
from ..models.matierepremiere import matierespremieres

api_matierespremieres = Blueprint('api_matierespremieres', __name__)


@api_matierespremieres.route('/api/matierespremieres')
def get_matierespremieres():
	return jsonify([
		{
			'id': matierepremiere.id, 'nom': matierepremiere.nom, 'type': matierepremiere.type,
			'composition': matierepremiere.composition
			} for matierepremiere in matierespremieres.query.all()
	])
		
@api_matierespremieres.route('/api/matierepremiere/<id>/')
def get_matierepremiere(id):
	print(id)
	matierepremiere = matierespremieres.query.filter_by(id=id).first_or_404()
	return {
		'id': matierepremiere.id, 'nom': matierepremiere.nom, 'type': matierepremiere.type,
			'composition': matierepremiere.composition
		}

@api_matierespremieres.route('/api/matierepremiere/add', methods=['POST'])
def create_matierepremiere():
	data = request.get_json()
	if not 'nom' in data or not 'type' in data:
		return jsonify({
			'error': 'Bad Request',
			'message': 'nom or type not given'
		}), 400
	if len(data['nom']) < 4 or len(data['type']) < 4:
		return jsonify({
			'error': 'Bad Request',
			'message': 'nom and type must be contain minimum of 4 letters'
		}), 400
	entry = matierespremieres(
			nom=data['nom'], 
			type=data['type'],
			composition=data['composition']
		)
	db.session.add(entry)
	db.session.commit()
	return {
		'id': entry.id, 'nom': entry.nom, 'type': entry.type,
			'composition': entry.composition
	}, 201

@api_matierespremieres.route('/api/matierepremiere/update/<id>', methods=['PUT'])
def update_matierepremiere(id):
	data = request.get_json()
	if 'nom' not in data:
		return {
			'error': 'Bad Request',
			'message': 'nom field needs to be present'
		}, 400
	matierepremiere = matierespremieres.query.filter_by(id=id).first_or_404()
	matierepremiere.nom=data['nom']
	matierepremiere.type=data['type']
	matierepremiere.composition=data['composition']
	

	
	db.session.commit()
	return jsonify({
		'id': matierepremiere.id, 'nom': matierepremiere.nom, 'type': matierepremiere.type,
			'composition': matierepremiere.composition
		})

@api_matierespremieres.route('/api/matierepremiere/delete/<id>', methods=['DELETE'] )
def delete_matierepremiere(id):
	matierepremiere = matierespremieres.query.filter_by(id=id).first_or_404()
	db.session.delete(matierepremiere)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}

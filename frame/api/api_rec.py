
from flask import request, Blueprint,jsonify
from frame import db
from ..models.recommandation import recommandations

api_recommandations = Blueprint('api_recommandations', __name__)


@api_recommandations.route('/api/recommandations')
def get_recommandations():
	return jsonify([
		{
			'id': recommandation.id, 'titre': recommandation.titre, 'description': recommandation.description,
			'domaine': recommandation.domaine,'specification': recommandation.specification,'retenu': recommandation.retenu,'etat': recommandation.etat,'date_ins': recommandation.date_ins
			} for recommandation in recommandations.query.all()
	])
		
@api_recommandations.route('/api/recommandation/<id>/')
def get_recommandation(id):
	print(id)
	recommandation = recommandations.query.filter_by(id=id).first_or_404()
	return {
		'id': recommandation.id, 'titre': recommandation.titre, 'description': recommandation.description,
			'domaine': recommandation.domaine,'specification': recommandation.specification,'retenu': recommandation.retenu,'etat': recommandation.etat,'date_ins': recommandation.date_ins
		}

@api_recommandations.route('/api/recommandation/add', methods=['POST'])
def create_recommandation():
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
	entry = recommandations(
			titre=data['titre'], 
			description=data['description'],
			domaine=data['domaine'],
			specification=data['specification'],
			retenu=data['retenu'],
			etat=data['etat']
			
		)
	db.session.add(entry)
	db.session.commit()
	return {
		'id': entry.id, 'titre': entry.titre, 'description': entry.description,
			'domaine': entry.domaine,'specification': entry.specification,'retenu': entry.retenu,'etat': entry.etat,'date_ins': entry.date_ins 
	}, 201

@api_recommandations.route('/api/recommandation/update/<id>', methods=['PUT'])
def update_recommandation(id):
	data = request.get_json()
	if 'titre' not in data:
		return {
			'error': 'Bad Request',
			'message': 'titre field needs to be present'
		}, 400
	recommandation = recommandations.query.filter_by(id=id).first_or_404()
	recommandation.titre=data['titre']
	recommandation.description=data['description']
	recommandation.domaine=data['domaine']
	recommandation.specification=data['specification']
	recommandation.retenu=data['retenu']
	recommandation.etat=data['etat']
	recommandation.date_ins=data['date_ins']
	
	db.session.commit()
	return jsonify({
		'id': recommandation.id, 'titre': recommandation.titre, 'description': recommandation.description,
			'domaine': recommandation.domaine,'specification': recommandation.specification,'retenu': recommandation.retenu,'etat': recommandation.etat,'date_ins': recommandation.date_ins
		})

@api_recommandations.route('/api/recommandation/delete/<id>', methods=['DELETE'] )
def delete_recommandation(id):
	recommandation = recommandations.query.filter_by(id=id).first_or_404()
	db.session.delete(recommandation)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}

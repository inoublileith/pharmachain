
from flask import request, Blueprint,jsonify
from frame import db
from ..models.analyste import analystes

api_analystes = Blueprint('api_analystes', __name__)


@api_analystes.route('/api/analystes')
def get_analystes():
	return jsonify([
		{
			'id': analyste.id, 'nom': analyste.nom, 'prenom': analyste.prenom
			} for analyste in analystes.query.all()
	])
		
@api_analystes.route('/api/analyste/<id>/')
def get_analyste(id):
	print(id)
	analyste = analystes.query.filter_by(id=id).first_or_404()
	return {
		'id': analyste.id, 'nom': analyste.nom, 'prenom': analyste.prenom
		}

@api_analystes.route('/api/analyste/add', methods=['POST'])
def create_analyste():
	data = request.get_json()
	if not 'nom' in data or not 'prenom' in data:
		return jsonify({
			'error': 'Bad Request',
			'message': 'nom or prenom not given'
		}), 400
	if len(data['nom']) < 4 or len(data['prenom']) < 4:
		return jsonify({
			'error': 'Bad Request',
			'message': 'nom and prenom must be contain minimum of 4 letters'
		}), 400
	entry = analystes(
			nom=data['nom'], 
			prenom=data['prenom']
			
		)
	db.session.add(entry)
	db.session.commit()
	return {
		'id': entry.id, 'nom': entry.nom, 'prenom': entry.prenom
	}, 201

@api_analystes.route('/api/analyste/update/<id>', methods=['PUT'])
def update_analyste(id):
	data = request.get_json()
	if 'nom' not in data:
		return {
			'error': 'Bad Request',
			'message': 'nom field needs to be present'
		}, 400
	analyste = analystes.query.filter_by(id=id).first_or_404()
	analyste.nom=data['nom']
	analyste.prenom=data['prenom']
	
	
	db.session.commit()
	return jsonify({
		'id': analyste.id, 'nom': analyste.nom, 'prenom': analyste.prenom
		})

@api_analystes.route('/api/analyste/delete/<id>', methods=['DELETE'] )
def delete_analyste(id):
	analyste = analystes.query.filter_by(id=id).first_or_404()
	db.session.delete(analyste)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}

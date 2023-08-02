
from flask import request, Blueprint,jsonify
from frame import db
from ..models.grossiste import grossistes

api_grossistes = Blueprint('api_grossistes', __name__)


@api_grossistes.route('/api/grossistes')
def get_grossistes():
	return jsonify([
		{
			'id': grossiste.id, 'nom': grossiste.nom, 'prenom': grossiste.prenom,
	        'tel': grossiste.tel
			} for grossiste in grossistes.query.all()
	])
		
@api_grossistes.route('/api/grossiste/<id>/')
def get_grossiste(id):
	print(id)
	grossiste = grossistes.query.filter_by(id=id).first_or_404()
	return {
		'id': grossiste.id, 'nom': grossiste.nom, 'prenom': grossiste.prenom,
		'tel': grossiste.tel
		}

@api_grossistes.route('/api/grossiste/add', methods=['POST'])
def create_grossiste():
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
	entry = grossistes(
			nom=data['nom'], 
			prenom=data['prenom'],
			tel=data['tel']
			
		)
	db.session.add(entry)
	db.session.commit()
	return {
		'id': entry.id, 'nom': entry.nom, 'prenom': entry.prenom,
		'tel': entry.tel
	}, 201

@api_grossistes.route('/api/grossiste/update/<id>', methods=['PUT'])
def update_grossiste(id):
	data = request.get_json()
	if 'nom' not in data:
		return {
			'error': 'Bad Request',
			'message': 'nom field needs to be present'
		}, 400
	grossiste = grossistes.query.filter_by(id=id).first_or_404()
	grossiste.nom=data['nom']
	grossiste.prenom=data['prenom']
	grossiste.tel=data['tel']
	
	db.session.commit()
	return jsonify({
		'id': grossiste.id, 'nom': grossiste.nom, 'prenom': grossiste.prenom,
		'tel': grossiste.tel
		})

@api_grossistes.route('/api/grossiste/delete/<id>', methods=['DELETE'] )
def delete_grossiste(id):
	grossiste = grossistes.query.filter_by(id=id).first_or_404()
	db.session.delete(grossiste)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}


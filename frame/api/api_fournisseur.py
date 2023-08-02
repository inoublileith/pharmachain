
from flask import request, Blueprint,jsonify
from frame import db
from ..models.fournisseur import fournisseurs

api_fournisseurs = Blueprint('api_fournisseurs', __name__)


@api_fournisseurs.route('/api/fournisseurs')
def get_fournisseurs():
	return jsonify([
		{
			'id': fournisseur.id, 'nom': fournisseur.nom, 'prenom': fournisseur.prenom,
	        'tel': fournisseur.tel
			} for fournisseur in fournisseurs.query.all()
	])
		
@api_fournisseurs.route('/api/fournisseur/<id>/')
def get_fournisseur(id):
	print(id)
	fournisseur = fournisseurs.query.filter_by(id=id).first_or_404()
	return {
		'id': fournisseur.id, 'nom': fournisseur.nom, 'prenom': fournisseur.prenom,
		'tel': fournisseur.tel
		}

@api_fournisseurs.route('/api/fournisseur/add', methods=['POST'])
def create_fournisseur():
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
	entry = fournisseurs(
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

@api_fournisseurs.route('/api/fournisseur/update/<id>', methods=['PUT'])
def update_fournisseur(id):
	data = request.get_json()
	if 'nom' not in data:
		return {
			'error': 'Bad Request',
			'message': 'nom field needs to be present'
		}, 400
	fournisseur = fournisseurs.query.filter_by(id=id).first_or_404()
	fournisseur.nom=data['nom']
	fournisseur.prenom=data['prenom']
	fournisseur.tel=data['tel']
	
	db.session.commit()
	return jsonify({
		'id': fournisseur.id, 'nom': fournisseur.nom, 'prenom': fournisseur.prenom,
		'tel': fournisseur.tel
		})

@api_fournisseurs.route('/api/fournisseur/delete/<id>', methods=['DELETE'] )
def delete_fournisseur(id):
	fournisseur = fournisseurs.query.filter_by(id=id).first_or_404()
	db.session.delete(fournisseur)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}


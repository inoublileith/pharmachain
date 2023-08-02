
from flask import request, Blueprint,jsonify
from frame import db
from ..models.patient import patients

api_patients = Blueprint('api_patients', __name__)


@api_patients.route('/api/patients')
def get_patients():
	return jsonify([
		{
			'id': patient.id, 'nom': patient.nom, 'prenom': patient.prenom,
			'email': patient.email,'tel': patient.tel
			} for patient in patients.query.all()
	])
		
@api_patients.route('/api/patient/<id>/')
def get_patient(id):
	print(id)
	patient = patients.query.filter_by(id=id).first_or_404()
	return {
		'id': patient.id, 'nom': patient.nom, 'prenom': patient.prenom,
			'email': patient.email,'tel': patient.tel
		}

@api_patients.route('/api/patient/add', methods=['POST'])
def create_patient():
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
	entry = patients(
			nom=data['nom'], 
			prenom=data['prenom'],
			email=data['email'],
			tel=data['tel']
			
		)
	db.session.add(entry)
	db.session.commit()
	return {
		'id': entry.id, 'nom': entry.nom, 'prenom': entry.prenom,
			'email': entry.email,'tel': entry.tel
	}, 201

@api_patients.route('/api/patient/update/<id>', methods=['PUT'])
def update_patient(id):
	data = request.get_json()
	if 'nom' not in data:
		return {
			'error': 'Bad Request',
			'message': 'nom field needs to be present'
		}, 400
	patient = patients.query.filter_by(id=id).first_or_404()
	patient.nom=data['nom']
	patient.prenom=data['prenom']
	patient.email=data['email']
	patient.tel=data['tel']
	
	db.session.commit()
	return jsonify({
		'id': patient.id, 'nom': patient.nom, 'prenom': patient.prenom,
			'email': patient.email,'tel': patient.tel
		})

@api_patients.route('/api/patient/delete/<id>', methods=['DELETE'] )
def delete_patient(id):
	patient = patients.query.filter_by(id=id).first_or_404()
	db.session.delete(patient)
	db.session.commit()
	return {
		'success': 'Data deleted successfully'
	}


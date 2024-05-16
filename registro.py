from app import app, db
from flask import request, jsonify, make_response
from model import Registro, registro_schema, registros_schema
from method import *

@app.route('/registro', methods=[POST])
def add_registro():
	numero_cedula = request.json['numero_cedula']
	new_registro = Registro(numero_cedula)
	db.session.add(new_registro)
	db.session.commit()
	return registro_schema.jsonify(new_registro)
	
@app.route('/registro', methods=[GET])
def get_registros():
	all_registros = Registro.query.all()
	result = registros_schema.dump(all_registros)
	return jsonify(result)

@app.route('/registro/<id>', methods=[GET])
def get_registro(id):
	registro = Registro.query.get(id)
	return registro_schema.jsonify(registro)

# actualizar el numero de identidad no tiene mucho sentido
# @app.route('/registro/<id>', methods=[PUT])
# def update_registro(id):
# 	registro = Registro.query.get(id)
# 	numero_cedula = request.json['numero_cedula']
# 	registro.numero_cedula = numero_cedula
# 	db.session.commit()
# 	return registro_schema.jsonify(registro)

@app.route('/registro/<id>', methods=[DELETE])
def delete_registro(id):
	registro = Registro.query.get(id)
	db.session.delete(registro)
	db.session.commit()
	return make_response(f'registro {id} deleted', 200)
from app import app, db
from flask import request, jsonify, make_response
from model import Notificacion, notificacion_schema, notificaciones_schema
from method import *

@app.route('/notificacion', methods=[POST])
def add_notificacion():
	numero_notificacion = request.json['numero_notificacion']
	numero_cedula = request.json['numero_cedula']
	comentarios = request.json['comentarios']
	ruta_fotografia = request.json['ruta_fotografia']
	coordenadas = request.json['coordenadas']
	
	new_notificacion = Notificacion(numero_notificacion, numero_cedula, comentarios, ruta_fotografia, coordenadas)
	db.session.add(new_notificacion)
	db.session.commit()
	return notificacion_schema.jsonify(new_notificacion)
	
@app.route('/notificacion', methods=[GET])
def get_all_notificaciones():
	all_notificaciones = Notificacion.query.all()
	result = notificaciones_schema.dump(all_notificaciones)
	return jsonify(result)

@app.route('/notificacion/<id>', methods=[GET])
def get_notificacion(id):
	notificacion = Notificacion.query.get(id)
	return notificacion_schema.jsonify(notificacion)

@app.route('/notificacion/<id>', methods=[PUT])
def update_notificacion(id):
	notificacion = Notificacion.query.get(id)
	comentarios = request.json['comentarios']
	ruta_fotografia = request.json['ruta_fotografia']
	coordenadas = request.json['coordenadas']
	
	notificacion.comentarios = comentarios
	notificacion.ruta_fotografia = ruta_fotografia
	notificacion.coordenadas = coordenadas
	
	db.session.commit()
	return notificacion_schema.jsonify(notificacion)

@app.route('/notificacion/<id>', methods=[DELETE])
def delete_notificacion(id):
	notificacion = Notificacion.query.get(id)
	db.session.delete(notificacion)
	db.session.commit()
	return make_response(f'notificacion {id} deleted', 200)
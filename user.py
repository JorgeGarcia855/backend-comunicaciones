from app import app, db
from flask import request, jsonify, make_response
from model import User, user_schema, users_schema
from method import *

@app.route('/user', methods=[POST])
def add_user():
	user_id = request.json['user_id']
	username = request.json['username']
	password = request.json['password']
	citizen_id = request.json['citizen_id']
	email = request.json['email']
	
	new_user = User(user_id,username,password,citizen_id,email)
	db.session.add(new_user)
	db.session.commit()
	return user_schema.jsonify(new_user)
	
@app.route('/user', methods=[GET])
def get_users():
	all_users = User.query.all()
	result = users_schema.dump(all_users)
	return jsonify(result)

@app.route('/user/<id>', methods=[GET])
def get_user(id):
	user = User.query.get(id)
	return user_schema.jsonify(user)

@app.route('/user/<id>', methods=[PUT])
def update_user(id):
	user = User.query.get(id)
	username = request.json['username']
	password = request.json['password']
	email = request.json['email']
	
	user.username = username
	user.password = password
	user.email = email
	
	db.session.commit()
	return user_schema.jsonify(user)

@app.route('/user/<id>', methods=[DELETE])
def delete_user(id):
	user = User.query.get(id)
	db.session.delete(user)
	db.session.commit()
	return make_response(f'user {id} deleted', 200)
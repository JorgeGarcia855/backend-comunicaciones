from app import app, db
from flask import request, jsonify, make_response
from model import EmailContent, content_schema, contents_schema
from method import *

@app.route('/email', methods=[POST])
def add_email():
	content_id = request.json['content_id']
	user_id = request.json['user_id']
	body = request.json['body']
	direction = request.json['direction']
	img_path = request.json['img_path']
	
	new_email = EmailContent(content_id,user_id,body,direction,img_path)
	db.session.add(new_email)
	db.session.commit()
	return content_schema.jsonify(new_email)
	
@app.route('/email', methods=[GET])
def get_all_emails():
	all_emails = EmailContent.query.all()
	result = contents_schema.dump(all_emails)
	return jsonify(result)

@app.route('/email/<id>', methods=[GET])
def get_email(id):
	email = EmailContent.query.get(id)
	return content_schema.jsonify(email)

@app.route('/email/<id>', methods=[PUT])
def update_email(id):
	email = EmailContent.query.get(id)
	body = request.json['body']
	direction = request.json['direction']
	img_path = request.json['img_path']
	
	email.body = body
	email.direction = direction
	email.img_path = img_path
	
	db.session.commit()
	return content_schema.jsonify(email)

@app.route('/email/<id>', methods=[DELETE])
def delete_email(id):
	email = EmailContent.query.get(id)
	db.session.delete(email)
	db.session.commit()
	return make_response(f'email {id} deleted', 200)
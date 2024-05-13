from app import db, ma
from marshmallow_sqlalchemy import fields

class User(db.Model):
	__tablename__ = "user"
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	password = db.Column(db.Text)
	citizen_id = db.Column(db.Integer, unique=True)
	email = db.Column(db.Text)
	contents = db.relationship("EmailContent", backref="user", lazy="dynamic")
	
	def __init__(self, user_id, username, password, citizen_id, email):
		self.user_id = user_id
		self.username = username
		self.password = password
		self.citizen_id = citizen_id
		self.email = email
		
class EmailContent(db.Model):
	__tablename__ = "email_content"
	content_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
	body = db.Column(db.Text)
	direction = db.Column(db.Text)
	img_path = db.Column(db.Text)
	
	def __init__(self, content_id, user_id, body, direction, img_path):
		self.content_id = content_id
		self.user_id = user_id
		self.body = body
		self.direction = direction
		self.img_path = img_path
	  
class EmailContentSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = EmailContent
		load_instance = True
		sqla_session = db.session
		include_relationships = True
		include_fk = True

class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User
		load_instance = True
		sqla_session = db.session
		include_relationships = True
	contents = fields.Nested(EmailContentSchema, many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
content_schema = EmailContentSchema()
contents_schema = EmailContentSchema(many=True)
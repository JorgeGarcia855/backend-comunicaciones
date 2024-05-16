from app import db, ma
from marshmallow_sqlalchemy import fields

class Registro(db.Model):
	__tablename__ = "registro"
	numero_cedula = db.Column(db.Integer, primary_key=True)
	notificaciones = db.relationship("Notificacion", backref="registro", lazy="dynamic")
	
	def __init__(self, numero_cedula):
		self.numero_cedula = numero_cedula
		
		
class Notificacion(db.Model):
	__tablename__ = "notificacion"
	numero_notificacion = db.Column(db.Integer, primary_key=True)
	numero_cedula = db.Column(db.Integer, db.ForeignKey('registro.numero_cedula'))
	comentarios = db.Column(db.Text)
	ruta_fotografia = db.Column(db.Text)
	coordenadas = db.Column(db.Text)
	
	def __init__(self, numero_notificacion, numero_cedula, comentarios, ruta_fotografia, coordenadas):
		self.numero_notificacion = numero_notificacion
		self.numero_cedula = numero_cedula
		self.comentarios = comentarios
		self.ruta_fotografia = ruta_fotografia
		self.coordenadas = coordenadas
	  
class NotificacionSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Notificacion
		load_instance = True
		sqla_session = db.session
		include_relationships = True
		include_fk = True

class RegistroSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Registro
		load_instance = True
		sqla_session = db.session
		include_relationships = True
	notificaciones = fields.Nested(NotificacionSchema, many=True)

registro_schema = RegistroSchema()
registros_schema = RegistroSchema(many=True)
notificacion_schema = NotificacionSchema()
notificaciones_schema = NotificacionSchema(many=True)
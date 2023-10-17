from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TestModel(db.Model):
	__tablename__ = "table"

	// add the fields
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String())
	comment = db.Column(db.String())
	
	def __init__(self, id, url, comment):
		self.id = id
		self.url = url
		self.comment = comment

	def __repr__(self):
		return f"{self.id}:{self.comment}"	
	

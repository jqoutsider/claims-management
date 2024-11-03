from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Assignment(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    claimId = db.Column(db.String(100), nullable=False)
    operatorId = db.Column(db.String(100), nullable=False)
    designedDate = db.Column(db.DateTime, nullable=False)
    processedDate = db.Column(db.DateTime, nullable=False)
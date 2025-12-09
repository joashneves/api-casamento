from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    attending = db.Column(db.Boolean, nullable=False)
    message = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<RSVP {self.name} - Attending: {self.attending}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'attending': self.attending,
            'message': self.message,
            'timestamp': self.timestamp.isoformat()
        }

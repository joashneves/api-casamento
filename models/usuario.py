from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.Boolean, nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'senha': self.senha
        }

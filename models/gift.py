from .rsvp import db

class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=True)
    link = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(255), nullable=True) # New field
    is_gifted = db.Column(db.Boolean, default=False, nullable=False)
    donor_name = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'link': self.link,
            'image_url': self.image_url, # New field
            'is_gifted': self.is_gifted,
            'donor_name': self.donor_name,
        }

from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    products = db.relationship('Product', backref='category', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Category {self.name}>'

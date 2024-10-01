from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    images = db.Column(db.PickleType, nullable=True)  # This assumes you're storing a list of image filenames

    def __init__(self, name, price, description, category_id, images=None):
        self.name = name
        self.price = price
        self.description = description
        self.category_id = category_id
        self.images = images or []

    def __repr__(self):
        return f'<Product {self.name}>'

from flask import Blueprint, render_template
from app.models.product import Product

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/<int:category_id>')
def list_products_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    return render_template('product.html', products=products)

@product_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

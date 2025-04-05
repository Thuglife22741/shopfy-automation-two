"""Controller for managing sales page creation in Shopify."""

from flask import Blueprint, jsonify, render_template
from ..tools.shopify_api import get_shop_info
from ..tools.shopify_integration import create_sales_page

sales_page_bp = Blueprint('sales_page', __name__, template_folder='../templates')

@sales_page_bp.route('/', methods=['GET'])
def show_sales_page():
    """Display the sales page."""
    try:
        shop_info = get_shop_info()
        return render_template('sales_page.html', shop=shop_info)
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erro ao carregar página de vendas: {str(e)}'
        }), 500

@sales_page_bp.route('/api/create-sales-page', methods=['POST'])
def create_shopify_sales_page():
    """Create a sales page in Shopify store."""
    try:
        result = create_sales_page()
        
        if result['success']:
            return jsonify({
                'status': 'success',
                'message': 'Página de vendas criada com sucesso!',
                'data': {
                    'product_id': result['product_id'],
                    'product_title': result['product_title'],
                    'product_url': f'https://sua-loja.myshopify.com/products/{result["product_handle"]}'
                }
            }), 200
        
        return jsonify({
            'status': 'error',
            'message': result['error']
        }), 400
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erro ao criar página de vendas: {str(e)}'
        }), 500
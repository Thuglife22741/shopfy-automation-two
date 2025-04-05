"""Module for Shopify store integration and sales page creation."""

from .product_data import get_product_data
from .shopify_session import initialize_shopify_session
from .product_images import optimize_images
from .shopify_api import create_product_from_url, initialize_shopify_session

def create_sales_page():
    """Create a sales page in Shopify store using product data."""
    try:
        # Initialize Shopify session and validate connection
        session = initialize_shopify_session()
        if not session:
            return {
                'success': False,
                'error': 'Falha ao conectar com a loja Shopify. Verifique suas credenciais.'
            }
        
        # Get product data with SEO optimization
        product_data = get_product_data()
        
        # Optimize product images
        optimized_images = optimize_images(product_data['images'])
        
        # Create enhanced product description
        enhanced_description = f"""
        <div class='product-description'>
            <h2>🌟 {product_data['title']} - Oferta Exclusiva!</h2>
            
            <div class='benefits'>
                <p>✨ Características Principais:</p>
                {product_data['description']}
            </div>
            
            <div class='guarantee'>
                <p>🔒 Garantia de Satisfação</p>
                <p>💫 Envio Rápido e Seguro</p>
                <p>🎁 Bônus Especial por Tempo Limitado</p>
            </div>
            
            <div class='cta'>
                <p>⚡ Aproveite esta oferta especial agora!</p>
                <p>🏃‍♂️ Últimas unidades disponíveis</p>
            </div>
        </div>
        """
        
        # Create product in Shopify with enhanced content
        result = create_product_from_url(
            title=f"🔥 {product_data['title']} | Oferta Especial",
            description=enhanced_description,
            price=product_data['price'],
            compare_at_price=float(product_data['price']) * 1.5,  # 50% markup for discount effect
            images=optimized_images,
            variants=product_data['variants']
        )
        
        if result:
            return {
                'success': True,
                'product_id': result['id'],
                'product_title': result['title'],
                'product_handle': result['handle']
            }
        
        return {
            'success': False,
            'error': 'Falha ao criar a página de vendas no Shopify'
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Erro ao criar página de vendas: {str(e)}'
        }
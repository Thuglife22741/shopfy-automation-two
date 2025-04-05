from src.crew_automation_for_shopify_e_commerce_integration.tools.post_automation import post_product_to_instagram
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Dados do produto para teste
produto = {
    'title': 'Camisa Masculina Estilosa',
    'price': '79.90',
    'url': 'https://iaseoshopfy.myshopify.com/products/camisa-masculina',
    'image_url': 'https://img.kwcdn.com/product/fancy/1145de29-72c2-4fc4-ba63-5f02467b7764.jpg'
}

def main():
    try:
        # Tentar fazer a postagem
        resultado = post_product_to_instagram(produto)
        
        if resultado['success']:
            print('Post criado com sucesso!')
            print(f'Mensagem: {resultado["message"]}')
        else:
            print('Erro ao criar o post')
            print(f'Erro: {resultado["message"]}')
            
    except Exception as e:
        print(f'Erro inesperado: {str(e)}')

if __name__ == '__main__':
    main()
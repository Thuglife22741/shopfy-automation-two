"""Script para criar um produto de teste na loja Shopify."""

import os
from dotenv import load_dotenv
from tools.shopify_api import create_product_from_url
from tools.shopify_session import initialize_shopify_session

def main():
    """Função principal para criar produto de teste."""
    try:
        # Carregar variáveis de ambiente
        load_dotenv()
        
        # Inicializar sessão Shopify
        session = initialize_shopify_session()
        if not session:
            print('Erro ao conectar com a loja Shopify')
            return
        
        # Obter URL e palavras-chave do arquivo .env
        url = os.getenv('CONCORRENTE_URL')
        keywords = os.getenv('PALAVRAS_CHAVE')
        
        if not url or not keywords:
            print('URL do concorrente ou palavras-chave não encontradas')
            return
        
        # Criar produto na loja Shopify
        result = create_product_from_url(url, keywords)
        
        if result:
            print('Produto criado com sucesso!')
            print(f'ID do produto: {result["id"]}')
            print(f'URL do produto: {result["url"]}')
        else:
            print('Erro ao criar o produto')
            
    except Exception as e:
        print(f'Erro: {str(e)}')

if __name__ == '__main__':
    main()
"""Module for managing Shopify API credentials."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Shopify API Credentials
SHOPIFY_CONFIG = {
    'shop_url': os.getenv('SHOPIFY_SHOP_URL', 'iaseoshopfy.myshopify.com'),
    'access_token': os.getenv('SHOPIFY_ADMIN_TOKEN'),
    'api_version': '2024-01',
    'api_key': os.getenv('SHOPIFY_API_KEY'),
    'api_secret': os.getenv('SHOPIFY_API_SECRET')
}

def get_shopify_credentials():
    """Get Shopify API credentials from environment."""
    return SHOPIFY_CONFIG
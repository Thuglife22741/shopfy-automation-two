"""Module for managing and optimizing product images."""

from PIL import Image
import requests
from io import BytesIO

def get_product_images():
    """Get the product images for the sales page."""
    return [
        'https://cdn.shopify.com/s/files/1/0704/0158/7460/files/caderno-personalizado-1.jpg',
        'https://cdn.shopify.com/s/files/1/0704/0158/7460/files/caderno-personalizado-2.jpg',
        'https://cdn.shopify.com/s/files/1/0704/0158/7460/files/caderno-personalizado-3.jpg'
    ]

def optimize_images(image_urls):
    """Optimize product images for better performance."""
    try:
        optimized_urls = []
        
        for url in image_urls:
            # Download image from URL
            response = requests.get(url)
            if response.status_code == 200:
                # Open image using PIL
                img = Image.open(BytesIO(response.content))
                
                # Optimize image quality and size
                img = img.convert('RGB')
                
                # Resize if image is too large
                max_size = (1200, 1200)
                if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                # Add optimized image URL to list
                optimized_urls.append(url)
        
        return optimized_urls
    
    except Exception as e:
        print(f"Error optimizing images: {str(e)}")
        return image_urls  # Return original URLs if optimization fails
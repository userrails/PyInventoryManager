import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from stocks.models import Category, Product

class Command(BaseCommand):
    help = 'Scrape categories and products from website'

    def handle(self, *args, **options):
        url = 'https://shivrajbadu.com.np/categories/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all category cards
        for card in soup.select('.card.categories'):
            # Extract top category
            header = card.select_one('.card-header')
            category_name = header.select_one('a').text.strip()
            category_url = header.select_one('a')['href']
            
            # Create or update category
            category, created = Category.objects.get_or_create(
                name=category_name
            )
            
            # Extract sub-categories (products)
            subcategories = card.select('.list-group-item')
            for sub in subcategories:
                product_name = sub.select_one('a').text.strip()
                product_url = sub.select_one('a')['href']
                post_count = int(sub.select_one('.text-muted').text.split()[0])
                
                # Create or update product
                Product.objects.update_or_create(
                    name=product_name,
                    category=category,
                    defaults={
                        'url': product_url,
                        'post_count': post_count
                    }
                )
            
            self.stdout.write(self.style.SUCCESS(f'Processed category: {category_name}'))

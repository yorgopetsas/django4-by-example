# import_books.py
import csv
# from datetime import datetime
from .models import Product

def import_books(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Product.objects.create(
                category = row['category'],
                name = row['name'],
                slug = row['slug'],
                image = row['image'],
                description = row['description'],
                price=row['price'],
                available = row['available'],
                created = row['created']
            )

if __name__ == '__main__':
    csv_file_path = 'product_import_test.csv'  # Replace with your actual file path
    import_books(csv_file_path)


    
    
    
    
    
    
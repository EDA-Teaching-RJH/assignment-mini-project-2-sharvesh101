import csv
import os

class FileManager:
    def __init__(self, inventory_file='inventory.csv', sales_file='sales_log.csv'):
        self.inventory_file = inventory_file
        self.sales_file = sales_file

    def load_inventory(self, inventory):
        if not os.path.exists(self.inventory_file):
            return
        with open(self.inventory_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['category'].lower() == 'electronics':
                    product = Electronics(
                        id=row['id'],
                        name=row['name'],
                        price=float(row['price']),
                        stock_quantity=int(row['stock_quantity']),
                        category=row['category'],
                        brand=row['brand'],
                        warranty_period=int(row['warranty_period'])
                    )
                else:
                    product = Product(
                        id=row['id'],
                        name=row['name'],
                        price=float(row['price']),
                        stock_quantity=int(row['stock_quantity']),
                        category=row['category']
                    )
                inventory.add_product(product)

    def save_inventory(self, inventory):
        with open(self.inventory_file, 'w', newline='') as f:
            fieldnames = ['id', 'name', 'price', 'stock_quantity', 'category', 'brand', 'warranty_period']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for p in inventory.products:
                row = {
                    'id': p.id,
                    'name': p.name,
                    'price': p.price,
                    'stock_quantity': p.stock_quantity,
                    'category': p.category,
                    'brand': getattr(p, 'brand', ''),
                    'warranty_period': getattr(p, 'warranty_period', '')
                }
                writer.writerow(row)

    def log_sale(self, product_id, quantity, total_price):
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        with open(self.sales_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, product_id, quantity, total_price])
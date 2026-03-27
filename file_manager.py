# file_manager.py
import csv
from product import Electronics


class FileManager:

    def __init__(self, filename):
        self.filename = filename

    def save_to_csv(self, products):

        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            # Write the header row first
            writer.writerow([
                "product_id", "name", "price",
                "quantity", "brand", "warranty_years", "category"
            ])
            # Write each product as a row
            for product in products:
                writer.writerow(product.to_csv_row())

        print(f"  Inventory saved to {self.filename}.")

    def load_from_csv(self):
        products = []

        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)   # reads rows as dictionaries
                for row in reader:
                    product = Electronics(
                        product_id=row["product_id"],
                        name=row["name"],
                        price=float(row["price"]),
                        quantity=int(row["quantity"]),
                        brand=row["brand"],
                        warranty_years=int(row["warranty_years"]),
                        category=row["category"]
                    )
                    products.append(product)

        except FileNotFoundError:
            print("  No existing inventory file found. Starting fresh.")

        return products
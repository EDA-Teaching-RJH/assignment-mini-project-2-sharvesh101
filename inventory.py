# inventory.py

class Inventory:
    def __init__(self):
        self.products = []          # list of Electronics objects

    def add_product(self, product):
        """Add a product to the inventory."""
        self.products.append(product)

    def remove_product(self, product_id):

        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return True
        return False

    def search(self, query):
        query = query.lower().strip()
        results = []
        for product in self.products:
            if query in product.name.lower():
                results.append(product)
        return results

    def list_all(self):
        return self.products

    def low_stock_alert(self, threshold=5):
        alerts = []
        for product in self.products:
            if product.quantity <= threshold:
                alerts.append(product)
        return alerts

    def find_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
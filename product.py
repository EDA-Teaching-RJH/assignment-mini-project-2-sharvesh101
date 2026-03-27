# product.py

class Product:

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        return (f"ID: {self.product_id} | Name: {self.name} | "
                f"Price: £{self.price:.2f} | Stock: {self.quantity}")

    def to_csv_row(self):
        return [self.product_id, self.name, self.price, self.quantity]


class Electronics(Product):

    def __init__(self, product_id, name, price, quantity, brand, warranty_years, category):
        # Call the parent class __init__ to set shared attributes
        super().__init__(product_id, name, price, quantity)
        self.brand = brand
        self.warranty_years = warranty_years
        self.category = category

    def display(self):
        base = super().display()
        return (f"{base} | Brand: {self.brand} | "
                f"Warranty: {self.warranty_years} yr(s) | Category: {self.category}")

    def to_csv_row(self):
        return [
            self.product_id,
            self.name,
            self.price,
            self.quantity,
            self.brand,
            self.warranty_years,
            self.category
        ]
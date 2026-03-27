# main.py
# Electronics Store Inventory System
from product import Electronics
from inventory import Inventory
from validators import is_valid_product_id, is_valid_price, is_valid_quantity, is_valid_warranty

def view_all_products(inventory):
    products = inventory.list_all()
 
    if not products:
        print("\n  No products in inventory.")
        return
 
    print("\n  {:<12} {:<20} {:<15} {:<10} {:<8} {}".format(
        "ID", "Name", "Brand", "Price", "Stock", "Category"))
    print("  " + "-" * 75)
 
    for p in products:
        print("  {:<12} {:<20} {:<15} £{:<9.2f} {:<8} {}".format(
            p.product_id, p.name, p.brand, p.price, p.quantity, p.category))

def add_product(inventory):
    """Ask the user for details and add a new Electronics product."""
    print("\n  -- Add New Product --")
 
    name = input("  Product name: ").strip()
    if not name:
        print("  Error: Name cannot be empty.")
        return
 
    brand = input("  Brand: ").strip()
    if not brand:
        print("  Error: Brand cannot be empty.")
        return
 
    category = input("  Category (e.g. Laptop, Phone, TV): ").strip()
    if not category:
        print("  Error: Category cannot be empty.")
        return
 
    price_input = input("  Price (e.g. 49.99): ").strip()
    if not is_valid_price(price_input):
        print("  Error: Invalid price. Please enter a positive number.")
        return
 
    quantity_input = input("  Stock quantity: ").strip()
    if not is_valid_quantity(quantity_input):
        print("  Error: Invalid quantity. Please enter a whole number.")
        return
 
    warranty_input = input("  Warranty (years, 1-5): ").strip()
    if not is_valid_warranty(warranty_input):
        print("  Error: Invalid warranty. Enter a number between 1 and 5.")
        return
 
    pid = generate_product_id(inventory)
 
    new_product = Electronics(
        product_id=pid,
        name=name,
        price=float(price_input),
        quantity=int(quantity_input),
        brand=brand,
        warranty_years=int(warranty_input),
        category=category
    )
 
    inventory.add_product(new_product)
    print(f"\n  Product added successfully! ID: {pid}")

while True:
    print("\n  ================================")
    print("   Electronics Store Inventory")
    print("  ================================")
    print("  1. View all products")
    print("  2. Add new product")
    print("  3. Remove product")
    print("  4. Search products")
    print("  5. Update stock quantity")
    print("  6. View low stock alerts")
    print("  7. Save & Exit")
    print("  ================================")

    choice = input("\n  Enter choice (1-7): ").strip()

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        print("\n  Goodbye!")
        break
    else:
        print("  Invalid choice. Please enter a number between 1 and 7.")
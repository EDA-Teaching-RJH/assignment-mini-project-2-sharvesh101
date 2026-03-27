# main.py
# Electronics Store Inventory System
import random
import datetime
import csv

from product import Electronics
from inventory import Inventory
from file_manager import FileManager
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

def remove_product(inventory):
    print("\n  -- Remove Product --")
    pid = input("  Enter product ID to remove (e.g. ELEC-001): ").strip().upper()
 
    if not is_valid_product_id(pid):
        print("  Error: Invalid product ID format. Use ELEC-### format.")
        return
 
    success = inventory.remove_product(pid)
    if success:
        print(f"  Product {pid} removed successfully.")
    else:
        print(f"  Error: Product {pid} not found.")

def search_products(inventory):
    print("\n  -- Search Products --")
    query = input("  Enter search term: ").strip()
 
    if not query:
        print("  Error: Search term cannot be empty.")
        return
 
    results = inventory.search(query)
 
    if not results:
        print(f"  No products found matching '{query}'.")
        return
 
    print(f"\n  Found {len(results)} result(s):")
    for p in results:
        print(f"  [{p.product_id}] {p.name} — {p.brand} — £{p.price:.2f} — Stock: {p.quantity}")

def update_stock(inventory):
    print("\n  -- Update Stock Quantity --")
    pid = input("  Enter product ID (e.g. ELEC-001): ").strip().upper()
 
    if not is_valid_product_id(pid):
        print("  Error: Invalid product ID format.")
        return
    product = inventory.find_by_id(pid)
    if not product:
        print(f"  Error: Product {pid} not found.")
        return
 
    print(f"  Current stock for '{product.name}': {product.quantity}")
    new_qty = input("  New quantity: ").strip()
 
    if not is_valid_quantity(new_qty):
        print("  Error: Invalid quantity.")
        return
 
    product.quantity = int(new_qty)
    print(f"  Stock updated to {product.quantity}.")

def view_low_stock(inventory):
    print("\n  -- Low Stock Alerts --")
    threshold_input = input("  Enter low stock threshold (press Enter for default 5): ").strip()
 
    if threshold_input == "":
        threshold = 5
    elif is_valid_quantity(threshold_input):
        threshold = int(threshold_input)
    else:
        print("  Error: Invalid threshold.")
        return
 
    alerts = inventory.low_stock_alert(threshold)
 
    if not alerts:
        print(f"  All products are above {threshold} units.")
        return
 
    print(f"\n  Products with {threshold} or fewer units in stock:")
    for p in alerts:
        print(f"  [{p.product_id}] {p.name} — Stock: {p.quantity}")

def save_and_exit(inventory, file_manager):
    """Save inventory to CSV, log the event, and exit."""
    file_manager.save_to_csv(inventory.products)
 
    # Write a timestamped entry to the sales log
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sales_log.csv", "a", newline="") as log:
        writer = csv.writer(log)
        writer.writerow([timestamp, "SAVE", "Inventory saved successfully"])
 
    print("  Goodbye!")

def main():
    file_manager = FileManager("inventory.csv")
    inventory = Inventory()
 
    # Load any existing products from CSV on startup
    loaded_products = file_manager.load_from_csv()
    for product in loaded_products:
        inventory.add_product(product)
 
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
            view_all_products(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            remove_product(inventory)
        elif choice == "4":
            search_products(inventory)
        elif choice == "5":
            update_stock(inventory)
        elif choice == "6":
            view_low_stock(inventory)
        elif choice == "7":
            save_and_exit(inventory, file_manager)
            break
        else:
            print("  Invalid choice. Please enter a number between 1 and 7.")
 
 
if __name__ == "__main__":
    import csv
    main()
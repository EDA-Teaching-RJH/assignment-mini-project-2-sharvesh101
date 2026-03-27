# main.py
# Electronics Store Inventory System
from inventory import Inventory

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
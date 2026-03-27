# test_inventory.py

from validators import is_valid_product_id, is_valid_price, is_valid_quantity, is_valid_warranty
from product import Product, Electronics
from inventory import Inventory

# ── Validator tests ───────────────────────────────────────────────────────────

def test_valid_product_id():
    assert is_valid_product_id("ELEC-001") == True
    assert is_valid_product_id("ELEC-999") == True
    assert is_valid_product_id("ELEC-123") == True
    print("  PASSED: test_valid_product_id")

def test_invalid_product_id():
    assert is_valid_product_id("elec-001") == False    
    assert is_valid_product_id("ELEC-01")  == False    
    assert is_valid_product_id("ELEC-1234") == False   
    assert is_valid_product_id("ELEC001")  == False    
    assert is_valid_product_id("")         == False    
    assert is_valid_product_id("ABCD-001") == False    
    print("  PASSED: test_invalid_product_id")

def test_valid_price():
    assert is_valid_price("49.99") == True
    assert is_valid_price("1")     == True
    assert is_valid_price("0.01")  == True
    assert is_valid_price("1000")  == True
    print("  PASSED: test_valid_price")

def test_invalid_price():
    assert is_valid_price("0")     == False    
    assert is_valid_price("-5")    == False    
    assert is_valid_price("abc")   == False    
    assert is_valid_price("")      == False    
    assert is_valid_price("£49")   == False    
    print("  PASSED: test_invalid_price")

def test_valid_quantity():
    assert is_valid_quantity("0")  == True     
    assert is_valid_quantity("10") == True
    assert is_valid_quantity("999") == True
    print("  PASSED: test_valid_quantity")

def test_invalid_quantity():
    assert is_valid_quantity("-1")  == False 
    assert is_valid_quantity("abc") == False   
    assert is_valid_quantity("1.5") == False   
    assert is_valid_quantity("")    == False   
    print("  PASSED: test_invalid_quantity")

def test_valid_warranty():
    assert is_valid_warranty("1") == True
    assert is_valid_warranty("3") == True
    assert is_valid_warranty("5") == True
    print("  PASSED: test_valid_warranty")

def test_invalid_warranty():
    assert is_valid_warranty("0")   == False   
    assert is_valid_warranty("6")   == False   
    assert is_valid_warranty("abc") == False   
    assert is_valid_warranty("")    == False   
    print("  PASSED: test_invalid_warranty")

# ── Product tests ─────────────────────────────────────────────────────────────

def test_electronics_inherits_product():
    e = Electronics("ELEC-001", "Laptop", 999.99, 10, "Dell", 2, "Laptop")
    assert isinstance(e, Product)        # Electronics IS a Product
    assert isinstance(e, Electronics)    # and also an Electronics
    print("  PASSED: test_electronics_inherits_product")

def test_product_display():
    e = Electronics("ELEC-002", "Phone", 499.99, 5, "Samsung", 1, "Phone")
    result = e.display()
    assert isinstance(result, str)
    assert "ELEC-002" in result
    assert "Phone" in result
    print("  PASSED: test_product_display")

def test_to_csv_row():
    e = Electronics("ELEC-003", "TV", 799.99, 3, "Sony", 3, "TV")
    row = e.to_csv_row()
    assert len(row) == 7
    assert row[0] == "ELEC-003"
    print("  PASSED: test_to_csv_row")

# ── Inventory tests ───────────────────────────────────────────────────────────

def test_add_product():
    inv = Inventory()
    e = Electronics("ELEC-010", "Tablet", 299.99, 8, "Apple", 1, "Tablet")
    inv.add_product(e)
    assert len(inv.products) == 1
    print("  PASSED: test_add_product")

def test_remove_product():
    inv = Inventory()
    e = Electronics("ELEC-011", "Headphones", 79.99, 15, "Sony", 1, "Audio")
    inv.add_product(e)
    result = inv.remove_product("ELEC-011")
    assert result == True
    assert len(inv.products) == 0
    print("  PASSED: test_remove_product")

def test_remove_nonexistent_product():
    inv = Inventory()
    result = inv.remove_product("ELEC-999")
    assert result == False
    print("  PASSED: test_remove_nonexistent_product")

def test_search_finds_match():
    inv = Inventory()
    e = Electronics("ELEC-012", "Gaming Laptop", 1299.99, 4, "Asus", 2, "Laptop")
    inv.add_product(e)
    results = inv.search("laptop")
    assert len(results) == 1
    assert results[0].product_id == "ELEC-012"
    print("  PASSED: test_search_finds_match")

def test_search_no_match():
    inv = Inventory()
    e = Electronics("ELEC-013", "Monitor", 349.99, 6, "LG", 2, "Display")
    inv.add_product(e)
    results = inv.search("keyboard")
    assert len(results) == 0
    print("  PASSED: test_search_no_match")

def test_low_stock_alert():
    inv = Inventory()
    low  = Electronics("ELEC-014", "Cable", 9.99,  2, "Anker", 1, "Accessory")
    high = Electronics("ELEC-015", "Speaker", 199.99, 20, "JBL", 2, "Audio")
    inv.add_product(low)
    inv.add_product(high)
    alerts = inv.low_stock_alert(5)
    assert len(alerts) == 1
    assert alerts[0].product_id == "ELEC-014"
    print("  PASSED: test_low_stock_alert")

# ── Run all tests ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n  Running all tests...\n")

    test_valid_product_id()
    test_invalid_product_id()
    test_valid_price()
    test_invalid_price()
    test_valid_quantity()
    test_invalid_quantity()
    test_valid_warranty()
    test_invalid_warranty()

    test_electronics_inherits_product()
    test_product_display()
    test_to_csv_row()

    test_add_product()
    test_remove_product()
    test_remove_nonexistent_product()
    test_search_finds_match()
    test_search_no_match()
    test_low_stock_alert()

    print("\n  All tests passed!")
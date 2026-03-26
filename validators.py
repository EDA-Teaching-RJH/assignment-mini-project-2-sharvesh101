def validate_id(id):
    if not id:
        return False, "ID cannot be empty."
    if not id.isalnum():
        return False, "ID must be alphanumeric."
    return True, ""

def validate_name(name):
    if not name:
        return False, "Name cannot be empty."
    if len(name) > 50:
        return False, "Name too long."
    return True, ""

def validate_price(price_str):
    try:
        price = float(price_str)
        if price < 0:
            return False, "Price cannot be negative."
        return True, ""
    except ValueError:
        return False, "Invalid price format."

def validate_stock(stock_str):
    try:
        stock = int(stock_str)
        if stock < 0:
            return False, "Stock cannot be negative."
        return True, ""
    except ValueError:
        return False, "Invalid stock format."

def validate_category(category):
    if not category:
        return False, "Category cannot be empty."
    return True, ""

def validate_brand(brand):
    if not brand:
        return False, "Brand cannot be empty."
    return True, ""

def validate_warranty(warranty_str):
    try:
        warranty = int(warranty_str)
        if warranty < 0:
            return False, "Warranty cannot be negative."
        return True, ""
    except ValueError:
        return False, "Invalid warranty format."
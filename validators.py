# validators.py

def is_valid_product_id(pid):
    parts = pid.split("-")      

    if len(parts) != 2:             
        return False
    if parts[0] != "ELEC":        
        return False
    if not parts[1].isdigit():      
        return False
    if len(parts[1]) != 3:         
        return False

    return True


def is_valid_price(price):
    try:
        value = float(price)       
        return value > 0            
    except ValueError:
        return False      


def is_valid_quantity(quantity):
    try:
        value = int(quantity)
        return value >= 0
    except ValueError:
        return False


def is_valid_warranty(warranty):
    try:
        value = int(warranty)
        return 1 <= value <= 5
    except ValueError:
        return False
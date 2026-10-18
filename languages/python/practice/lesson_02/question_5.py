def calculate_total_cents(quantity, price_cents):
    total_cents = quantity * price_cents
    return total_cents

def print_situation(name, quantity, price_cents):
    total_cents = calculate_total_cents(quantity, price_cents)
    print(f"Product Name = {name}, Quantity = {quantity}, Price Cents = {price_cents}, Total Cents = {total_cents}")


product_name = "Notebook"
quantity = 3
price_cents = 250

print_situation(product_name, quantity, price_cents)
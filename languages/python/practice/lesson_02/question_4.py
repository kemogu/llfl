def calculate_total_cents(quantity, price_cents):
    total_cents = quantity * price_cents
    return total_cents

def print_situation(quantity, price_cents):
    total_cents = calculate_total_cents(quantity, price_cents)
    print(f"Quantity = {quantity}, Price Cents = {price_cents}, Total Cents = {total_cents}")

quantity = 3
price_cents = 250

print_situation(quantity, price_cents)

quantity = quantity + 1

print_situation(quantity, price_cents)


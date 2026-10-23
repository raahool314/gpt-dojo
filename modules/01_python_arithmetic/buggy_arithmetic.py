"""Buggy arithmetic — find and fix every mistake."""

# --- Inputs ---

item_price = 12.50
quantity = 4

subtotal = 50.00
tax_rate_pct = 8.5

celsius = 25

a, b, c = 10, 20, 30


# --- Buggy computations ---

# Total cost
# total cost is the product of item_price and quantity not their difference
total_cost = item_price * quantity

# Tax amount
# tax amount is the product of subtotal and tax percentage divided by 100
tax_amount = subtotal * tax_rate_pct / 100

# Final price
# final price is the total_cost plus the tax_amount
final_price = total_cost + tax_amount


# Celsius to Fahrenheit:  F = C * 9/5 + 32
fahrenheit = (celsius * 9/5) + 32

# Average
# Fixing the problem using brackets
average = (a + b + c) / 3

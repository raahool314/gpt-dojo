"""Module 01 — Variables, types & arithmetic.

Replace each None below with the correct expression.
Do not change the input values.
"""

# --- Inputs (do not change these lines) ---

item_price = 12.50
quantity = 4

subtotal = 50.00
tax_rate_pct = 8.5  # percent, e.g. 8.5 means 8.5%

celsius = 25

a, b, c = 10, 20, 30


# --- Computations (replace None with an expression) ---

# 1. Total cost = item price * quantity
# total_cost = None
total_cost = item_price * quantity

# 2. Tax amount = subtotal * (tax_rate_pct / 100)
# tax_amount = None
tax_amount = subtotal * tax_rate_pct / 100

# 3. Final price = subtotal + tax_amount
# final_price = None
final_price = total_cost + tax_amount

# 4. Convert Celsius to Fahrenheit:  F = C * 9/5 + 32
# fahrenheit = None
fahrenheit = (celsius * (9/5)) + 32

# 5. Average of three numbers
# average = None
average = (a + b + c ) / 3


distance_leg1 = 18 * 2.5
distance_leg2 = 12 * 1.5
total_distance = distance_leg1 + distance_leg2
total_time = 2.5 + 1.5
average_speed = total_distance / total_time

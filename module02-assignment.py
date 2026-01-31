# Integrative Assignment: Module 2 – Type Conversion, Expressions, and Business Computations

# Step 1: Define variables
product_name = "Laptop Computer"  # Example product
units_sold_str = "25"  # Number of units as a string
price_per_unit_str = "899.99"  # Price as a string
tax_rate = 0.08  # 8% tax
discount_rate = 0.10  # 10% discount

# TODO: Convert string values to appropriate numeric types
units_sold = int(units_sold_str) #change units sold to integer
price_per_unit = float(price_per_unit_str) #change units sold to float
# TODO: Calculate taxed_price (original price + tax)
# Hint: taxed_price = price_per_unit * (1 + tax_rate)
taxed_price = price_per_unit * (1 + tax_rate) #calculate taxed_price
# TODO: Calculate net_price (taxed price - discount)
# Hint: net_price = taxed_price * (1 - discount_rate)
net_price = taxed_price * (1 - discount_rate) #calculate net_price
# TODO: Calculate total_revenue
total_revenue = net_price * units_sold #calculate the total revenue
# TODO: Display summary using f-string
print("Product :", product_name) #print the product name
print(f"Net price: ${net_price:.2f}") #print the net price with 2 decimal places
print(f"Total Revenue: ${total_revenue:.2f}") #print total revenue with 2 decimal places

    
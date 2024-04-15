# create a product and price for three items
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# create a company name and information
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# declare ending message
message = "Thanks for shopping with us today!"

# create a top border
print("*" * 50)

# print company information first, using format
print("* {:^46} *".format(company_name.title()))
print("* {:^46} *".format(company_address))
print("* {:^46} *".format(company_city))

# print a line between sections
print("=" * 50)

# print out header for section of items
print("* {:<20} {:>20} *".format("Product Name", "Product Price"))

# create a print statement for each product
print("* {:<20} ${:>19.2f} *".format(p1_name.title(), p1_price))
print("* {:<20} ${:>19.2f} *".format(p2_name.title(), p2_price))
print("* {:<20} ${:>19.2f} *".format(p3_name.title(), p3_price))

# print a line between sections
print("=" * 50)

# calculate total price and print out
total = p1_price + p2_price + p3_price
print("* {:<20} ${:>19.2f} *".format("Total", total))

# print a line between sections
print("=" * 50)

# output thank you message
print("* {:^46} *".format(message))

# create a bottom border
print("*" * 50)

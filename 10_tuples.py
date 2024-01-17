'''tuples are immutable

we use 1st bracket
'''

dimensions=(200,50)
print(type(dimensions))
#tuble cann't be changed
# dimensions[0]=100

print(dimensions)
# Define a tuple with five basic foods
menu = ("pizza", "burger", "pasta", "salad", "ice cream")

# Use a for loop to print each food the restaurant offers
print("Original menu:")
for food in menu:
    print(type(food))

# Try to modify one of the items (Python will raise an error)
# Uncomment the line below to see the error
# menu[0] = "sushi"

# The restaurant changes its menu, replacing two items
new_menu = ("sushi", "steak", "pasta", "soup", "cake")

# Rewrite the tuple to update the menu
menu = new_menu

# Use a for loop to print each of the items on the revised menu
print("\nRevised menu:")
for food in menu:
    print(food)


'''the problem is i dont exactly understand tuples all i have dont
i have watch you tube video to understand it '''



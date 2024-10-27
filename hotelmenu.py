'''
# define the menu of the restaurant using dictionary
menu={
    'Pizza':500,
    'Burger':240,
    'Sandwich':350,
    'Salad':480,
    'Fries':170,
    'Coffee':200,
    'Mojito':190,
    'Soft Drinks':40
}
#lets greet the customer
print("Welcome to the PYTHON Restaurant\nHope you are doing well!\nWhat can I serve you today? Here's the menu.")
print("Pizza : Rs 500\nBurger : Rs 240\nSandwich : Rs 350\nSalad : Rs 480\nFries : Rs 170\nCoffee : Rs 200\nMojito : Rs 190\nSoft Drinks : Rs 40\n")
order_total=0
item_1=input("Enter the name of the dish you want to order:")
if item_1 in menu:
    order_total+=menu[item_1];
    print(f"{item_1} has been added to your order")
else:
    print("Sorry, We are not serving this currently")
another_order=input("Would you like something else to be ordered? (YES/NO)").strip().lower()
if another_order == "yes":
    item_2=input("Enter the name of the dish that you want to order")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"{item_2} has been added to your order")
    else:
        print("Sorry, We are not serving this currently")
print(f"Your total amount to be paid is : {order_total}")

'''

menu = {
    'Pizza': 500,
    'Burger': 240,
    'Sandwich': 350,
    'Salad': 480,
    'Fries': 170,
    'Coffee': 200,
    'Mojito': 190,
    'Soft Drinks': 40
}

print("Welcome to the PYTHON Restaurant\nHope you are doing well!\nWhat can I serve you today? Here's the menu:")
for item, price in menu.items():
    print(f"{item} : Rs {price}")

order_total = 0

while True:
    item = input("Enter the name of the dish you want to order: ").strip()
    if item in menu:
        order_total += menu[item]
        print(f"{item} has been added to your order")
    else:
        print("Sorry, we are not serving this currently")
    
    another_order = input("Would you like to order something else? (YES/NO): ").strip().lower()
    if another_order != "yes":
        break

print(f"Your total amount to be paid is: Rs {order_total}")

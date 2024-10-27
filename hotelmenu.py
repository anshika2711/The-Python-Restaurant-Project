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

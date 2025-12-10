Menu = {
    "cheeseburger":15.00,
    "chicken burger":20.00,
    "Small soft drink":4.00,
    "Large soft drink":5.00,
}

GST =0.10

def order(menu):
    order = {}
    print("Please place your order. Enter quantity for each item.")
    for item, price in menu.items():
        while True:
            try:
                qty = int(input(f"No of {item}s: "))
                break
            except ValueError:
                print("Please enter a whole number (0 or greater).")
        if qty < 0:
            print("Negative quantity not allowed; setting to 0.")
            qty = 0
        order[item] = qty
    return order
if __name__ == "__main__":
    print("Welcome to the Redcat Shop!")
    print("Here is our menu:")
    user_order = order(Menu)
    print("Your order:", user_order)
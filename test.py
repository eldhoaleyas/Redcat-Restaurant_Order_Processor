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
            s = input(f"No of {item}s: ").strip()
            if s == "":
                qty = 0
                break
            try:
                qty = int(s)
                break
            except ValueError:
                print("Please enter a whole number (0 or greater), or press Enter for 0.")
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
    subtotal = sum(Menu[item] * qty for item, qty in user_order.items())
    print(f"Subtotal: ${subtotal:.2f}")
    
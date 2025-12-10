Menu = {
    "Cheeseburger":15.00,
    "Chicken burger":20.00,
    "Soft Drink (Small)":4.00,
    "Soft Drink (Large)":5.00,
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
    
    subtotal = sum(Menu[item] * qty for item, qty in user_order.items())
    

    # x+0.1x = subtotal --> x(1+0.1) = subtotal --> x = subtotal/1.1
    base_price = subtotal / (1 + GST)
    gst_amount = subtotal - base_price
    

    print("——————————————————————————")
    for item, qty in user_order.items():
        if qty > 0:
            # item_total = Menu[item] * qty
            # print(f"{qty} x {item} @ ${Menu[item]:.2f} each: ${item_total:.2f}")
            print(f"{item} x {qty} : ${Menu[item] * qty:.2f}")
    subtotal = sum(Menu[item] * qty for item, qty in user_order.items())
    print("\n\n")
    print("Total", f"${subtotal:.2f}")
    print("Including GST (10%)", f"${gst_amount:.2f}")
    
    print("——————————————————————————")
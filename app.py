import streamlit as st
Menu = {
    "Cheeseburger":15.00,
    "Chicken burger":20.00,
    "Soft Drink (Small)":4.00,
    "Soft Drink (Large)":5.00,
}

GST =0.10
input_entries = {}



def calculate_order(user_order, Menu, GST):
    
    items_for_receipt = []
    subtotal = 0
    for item_name, quantity in user_order.items():
        price = Menu[item_name] 
        inclusive_total = price * quantity      
        subtotal += inclusive_total
        item_data = {
            'name': item_name,
            'quantity': quantity,
            'inclusive_total': inclusive_total
        }
        items_for_receipt.append(item_data)
    
    base_price = subtotal / (1 + GST)
    gst_amount = subtotal - base_price
    return items_for_receipt, subtotal, gst_amount

st.title("Redcat Restaurant Order Processor")



with st.form("order_form"):
    st.subheader("Menu and Quantity")
    order_quantities = {}

  
    for item, price in Menu.items():
        quantity = st.number_input(f"{item} (${price:.2f})", min_value=0, step=1, value=0, key=item)
        order_quantities[item] = quantity

    # st.form_submit_button("Process Order & Show Receipt")
    submitted = st.form_submit_button("Process Order & Show Receipt")
    # submitted =False

    if submitted:
        final_order = {k: v for k, v in order_quantities.items() if v > 0}
        
        if final_order:
            line_items, total_inclusive, total_gst = calculate_order(final_order, Menu, GST)
            
            st.code("—" * 35) 
            for item in line_items:
                st.write(f"{item['name']} x {item['quantity']} ${item['inclusive_total']:.2f}")

            st.markdown(f"**Total: ${total_inclusive:.2f}**")
            st.text(f"Including GST (${total_gst:.2f})")
            st.code("—" * 35)
        else:
            st.warning("Please add at least one item to the order.")
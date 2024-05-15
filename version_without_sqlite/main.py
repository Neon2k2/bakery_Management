import pandas as pd


class Order:

    order_id = 1
    def __init__(self, customer, item, quantity):
        self.order_id = Order.order_id
        self.item = item
        self.customer = customer
        self.quantity = quantity
        Order.order_id += 1


Orders = []

def Add_Order():
    customer = input("Enter Customer Name: ")
    item = input("Enter item: ")
    quantity = int(input("Enter quantity: "))  # Convert quantity to integer
    if isinstance(quantity, int) and isinstance(customer, str):
        new_order = Order(customer, item, quantity)
        Orders.append(new_order)  # Append to Orders list, not Order
        print("Order successfully added.")
    else:
        print("Please enter the correct order details.")

def View_Orders():
    if not Orders:
        print("No orders to display.")
        return
    print("-" * 55)
    print("Order Id | Customer | Item | Quantity")
    print("-" * 55)
    for order in Orders:
        print(f"{order.order_id:<9} | {order.customer:<8} | {order.item:<4} | {order.quantity:<8}")
    print("-" * 55)

def Save_to_excel():
    if not Orders:
        print("No orders to save.")
        return
    df = pd.DataFrame([vars(order) for order in Orders])
    excel_filename = "orders.xlsx"
    df.to_excel(excel_filename, index=False)
    print("File successfully created!")

def Update_Order():
    customer = input("Enter customer name: ")
    item = input("Enter the Item: ")
    quantity = int(input("Enter the Quantity: "))
    for order in Orders:
        if order.customer == customer:
            order.item = item
            order.quantity = quantity
            print("Order updated successfully.")
            return
    print("Customer is not present in the records.")



choices = {
    1: Add_Order,
    2: View_Orders,
    3: Update_Order,
    4: Save_to_excel
}

if __name__ == "__main__":
    choice = 0  # Initialize choice
    while choice != 5:
        print("1. Add Order")
        print("2. View Order")
        print("3. Update Order")
        print("4. Save to Excel")
        print("5. Exit")

        print("-" * 25)
        choice = int(input("Enter your Choice: "))
        if choice in choices:
            choices[choice]()
        else:
            print("Invalid choice. Please select a valid option.")
























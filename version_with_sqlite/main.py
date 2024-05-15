import sqlite3
import pandas as pd


class Order:

    order_id = 1
    def __init__(self, customer, item, quantity):
        self.order_id = Order.order_id
        self.item = item
        self.customer = customer
        self.quantity = quantity
        Order.order_id += 1


def initialize_database():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY,
                    customer TEXT,
                    item TEXT,
                    quantity INTEGER
                )'''
    c.execute(query)
    conn.commit()
    conn.close()


def add_order():
    customer = input("Enter the name of the customer: ")
    item = input("Enter the item: ")
    quantity = input("Enter the quantity: ")

    if isinstance(customer, str)and isinstance(item, str):
        with sqlite3.connect('orders.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO orders (customer, item, quantity ) VALUES (?,?,?)", (customer, item, int(quantity)))
            connection.commit()

        print("order added successfully")
    else:
        print("Please enter the correct Order details...")


def view_order():

    with sqlite3.connect('orders.db') as connection:
        df = pd.read_sql_query("SELECT * FROM orders", connection)
        if df.empty:
            print("No orders found.")
        else:
            print(df)

def update_order():
    customer = input("name of the customer: ")
    item = input("Enter the item name: ")
    quantity = input("Enter the quantity: ")

    if isinstance(customer, str)and isinstance(item, str):
        with sqlite3.connect("orders.db") as connection:
            cursor = connection.cursor()

            cursor.execute("UPDATE orders SET item = ?, quantity = ? WHERE customer = ?", (item, int(quantity), customer))

            if cursor.rowcount == 0:
                print("No order found for this customer.")
            else:
                connection.commit()
                print("Order updated successfully.")
    else:
        print("PLease Enter the correct details...")

def export_excel():

    with sqlite3.connect("orders.db") as connection:
        df = pd.read_sql_query("SELECT * FROM orders", connection)
    if df.empty:
        print("No orders to export")
    else:
        df.to_excel("orders.xlsx", index=False)
        print("file successfully created")

choices = {
    1: add_order,
    2: view_order,
    3: update_order,
    4: export_excel
}



if __name__ == "__main__":
    initialize_database()

    while True:
        print("1. Add Order")
        print("2. View Orders")
        print("3. Update Order")
        print("4. Save to Excel")
        print("5. Exit")

        print("-" * 25)
        choice = input("Enter your Choice: ")

        if choice == '5':
            break

        if choice.isdigit():
            choice = int(choice)
            if choice in choices:
                choices[choice]()
            else:
                print("Invalid choice. Please select a valid option.")
        else:
            print("Invalid input. Please enter a number.")
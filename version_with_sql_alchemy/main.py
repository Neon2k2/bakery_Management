from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer = Column(String)
    item = Column(String)
    quantity = Column(Integer)


engine = create_engine('sqlite:///orders.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_order():
    customer = input("Enter the name of the customer: ")
    item = input("Enter the item: ")
    quantity = input("Enter the quantity: ")

    if isinstance(customer, str) and isinstance(item, str):
        order = Order(customer=customer, item=item, quantity=int(quantity))
        session.add(order)
        session.commit()
        print("Order added Successfully!!!")
    else:
        print("Please enter the correct order details!!")

def update_order():
    customer = Input("Enter the name of the customer: ")

    order = session.query(Order).filter(Order.customer == customer).first()

    if order is None:
        print("No order found for this customer")
    else:
        item = input("Enter the item name: ")
        quantity = input("Enter the quantity: ")

        order.item = item
        order.quantity = quantity
        session.commit()
        print("Order updated successfully")

def view_order():

    orders = session.query(Order).all()
    if not orders:
        print("No Orders found.")
    else:
        df = pd.DataFrame([{'id': order.id, 'customer': order.customer, 'item': order.item, 'quantity': order.quantity} for order in orders])
        print(df)

def export_excel():

    orders = session.query(Order).all()
    if not orders:
        print("No orders to export.")
    else:
        df = pd.DataFrame([{'id': order.id, 'customer': order.customer, 'item': order.item, 'quantity': order.quantity} for order in orders])
        excel_filename = "orders.csv"
        df.to_csv(excel_filename, index=False)
        print("Order successfully exported to csv")


choices = {
    1: add_order,
    2: view_order,
    3: update_order,
    4: export_excel
}


if __name__ == "__main__":

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
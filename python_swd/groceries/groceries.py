
# class Customer():
#     def __init__(self,cust_id: int,name: str,
#                 street: str,city: str,state: str,
#                 zip: str,phone: str,email: str):
#         self.cust_id = cust_id
#         self.name = name
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip = zip
#         self.phone = phone
#         self.email = email

#     def read_customers(file):
#         pass

# class Item():
#     pass

#     def read_items(file):
#         pass

# class Order():
#     def __init__(self, order_id: int, order_date, cust_id: int, line_items: list, payment: Payment) -> None:
#         pass

#     def read_orders(file):
#         pass

# class Payment():
#     pass

# class LineItem():
#     pass

# def main():
#     Customer.read_customers("customers.txt")
#     Item.read_items("items.txt")
#     Order.read_orders("orders.txt")

# if __name__ == '__main__':
#     main()
#     # Now print orders to the file order_report.txt

from dataclasses import dataclass, field
from typing import Dict, List
from collections import defaultdict

@dataclass
class Customer:
    customer_id: int
    name: str
    street: str
    city: str
    state: str
    zip_code: str
    phone: str
    email: str

    customers: Dict[int, 'Customer'] = field(default_factory=dict)

    def __str__(self):
        return f"{self.name}, ph. {self.phone}, email: {self.email}\n{self.street}\n{self.city}, {self.state} {self.zip_code}"

    @classmethod
    def read_customers(filename: str):
        with open(filename, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                customer = Customer(int(fields[0]), fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7])
                Customer.customers[customer.customer_id] = customer

@dataclass
class Item:
    item_id: int
    description: str
    price: float

    items: Dict[int, 'Item'] = field(default_factory=dict)

    @staticmethod
    def read_items(filename: str):
        with open(filename, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                item = Item(int(fields[0]), fields[1], float(fields[2]))
                Item.items[item.item_id] = item

@dataclass
class LineItem:
    item_id: int
    quantity: int

@dataclass
class Payment:
    payment_code: int

    def __str__(self):
        return ""

@dataclass
class CreditCard(Payment):
    card_number: str
    expiration_date: str

    def __str__(self):
        return f"Paid by Credit card {self.card_number}, exp. {self.expiration_date}"

@dataclass
class PayPal(Payment):
    paypal_id: str

    def __str__(self):
        return f"Paid by PayPal ID: {self.paypal_id}"

@dataclass
class WireTransfer(Payment):
    bank_id: str
    account_id: str

    def __str__(self):
        return f"Paid by Wire transfer from Bank ID {self.bank_id}, Account# {self.account_id}"

@dataclass
class Order:
    customer_id: int
    order_number: int
    order_date: str
    line_items: List[LineItem]
    payment: Payment

    orders: List['Order'] = field(default_factory=list)


    @property
    def total(self):
        return sum(Item.items[line.item_id].price * line.quantity for line in self.line_items)

    @staticmethod
    def read_orders(filename: str):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                order_fields = lines[i].strip().split(',')
                customer_id, order_number, order_date = map(int, order_fields[:3])
                item_quantity_pairs = order_fields[3:]
                line_items = [LineItem(int(item.split('-')[0]), int(item.split('-')[1])) for item in item_quantity_pairs]
                payment_fields = lines[i + 1].strip().split(',')
                payment_code = int(payment_fields[0])
                if payment_code == 1:
                    payment = CreditCard(payment_code, payment_fields[1], payment_fields[2])
                elif payment_code == 2:
                    payment = PayPal(payment_code, payment_fields[1])
                elif payment_code == 3:
                    payment = WireTransfer(payment_code, payment_fields[1], payment_fields[2])
                order = Order(customer_id, order_number, order_date, line_items, payment)
                Order.orders.append(order)

    def __str__(self):
        customer = Customer.customers[self.customer_id]
        lines = [f"Item {line.item_id}: \"{Item.items[line.item_id].description}\", {line.quantity} @ {Item.items[line.item_id].price:.2f}" for line in sorted(self.line_items, key=lambda x: x.item_id)]
        order_detail = "\n".join(lines)
        return f"===========================\nOrder #{self.order_number}, Date: {self.order_date}\nAmount: ${self.total:.2f}, {self.payment}\n\nCustomer ID #{self.customer_id}:\n{customer}\n\nOrder Detail:\n{order_detail}\n"

if __name__ == '__main__':
    Customer.read_customers("./customers.txt")
    Item.read_items("./items.txt")
    Order.read_orders("./orders.txt")

    with open("./order_report.txt", "w") as report_file:
        for order in Order.orders:
            report_file.write(str(order))

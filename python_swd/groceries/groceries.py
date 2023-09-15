from typing import List

class Customer:
    customers = {}

    def __init__(self, customer_id, name, street, city, state, zip_code, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    @classmethod
    def read_customers(cls, filename):
        with open(filename, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                customer = cls(int(fields[0]), fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7])
                cls.customers[customer.customer_id] = customer

    def __str__(self):
        return f"{self.name}, ph. {self.phone}, email: {self.email}\n{self.street}\n{self.city}, {self.state} {self.zip_code}"


class Item:
    items = {}

    def __init__(self, item_id, description, price):
        self.item_id = item_id
        self.description = description
        self.price = price

    @staticmethod
    def read_items(filename):
        with open(filename, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                item = Item(int(fields[0]), fields[1], float(fields[2]))
                Item.items[item.item_id] = item


class LineItem:
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity


class Payment:
    def __init__(self, payment_code):
        self.payment_code = payment_code

    def __str__(self):
        return ""


class CreditCard(Payment):
    def __init__(self, payment_code, card_number, expiration_date):
        super().__init__(payment_code)
        self.card_number = card_number
        self.expiration_date = expiration_date

    def __str__(self):
        return f"Paid by Credit card {self.card_number}, exp. {self.expiration_date}"


class PayPal(Payment):
    def __init__(self, payment_code, paypal_id):
        self.payment_code = payment_code
        self.paypal_id = paypal_id

class WireTransfer(Payment):

    def __init__(self, payment_code, bank_id: str, account_id: str):
        self.bank_id = bank_id
        self.payment_code = payment_code
        self.account_id = account_id

    def __str__(self):
        return f"Paid by Wire transfer from Bank ID {self.bank_id}, Account# {self.account_id}"


class Order:
    orders = []

    def __init__(self, customer_id: int, order_number: int, order_date: str, line_items: List[LineItem], payment: Payment) -> None:
        self.customer_id = customer_id
        self.order_number = order_number
        self.order_date = order_date
        self.line_items = line_items
        self.payment = payment

    @property
    def total(self):
        return sum(Item.items[line.item_id].price * line.quantity for line in self.line_items)

    @staticmethod
    def read_orders(filename: str):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                order_fields = lines[i].strip().split(',')
                customer_id, order_number = map(int, order_fields[:2])
                order_date = order_fields[2]
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

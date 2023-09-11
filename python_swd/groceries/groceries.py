
class Customer():
    pass
    def __init__(self,cust_id: int,name: str,
                street: str,city: str,state: str,
                zip: str,phone: str,email: str):
        self.cust_id = cust_id
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

    def read_customers(file):
        pass

class Item():
    pass

    def read_items(file):
        pass

class Order():
    pass

    def read_orders(file):
        pass

def main():
    Customer.read_customers("customers.txt")
    Item.read_items("items.txt")
    Order.read_orders("orders.txt")

if __name__ == '__main__':
    main()
    # Now print orders to the file order_report.txt
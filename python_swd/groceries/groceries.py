
class Customer():
    pass

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
class ShoppingCart:
    def __init__(self):
        self.products = []
        self.tax_rate = 0.0

    def add_product(self, product):
        for existing_product in self.products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                return
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def update_quantity(self, product_name, new_quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity = new_quantity

    def calculate_subtotal(self):
        return sum([product.price_per_unit * product.quantity for product in self.products])

    def set_tax_rate(self, tax_rate):
        self.tax_rate = tax_rate

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_cart(self):
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price_per_unit}, Quantity: {product.quantity}")
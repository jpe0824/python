import unittest
from product import Product
from shopping_cart import ShoppingCart
from unittest.mock import patch, call

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.product1 = Product("Apple", 1.0, 5)
        self.product2 = Product("Banana", 0.5, 10)
    def test_add_product(self):
        self.cart.add_product(self.product1)
        self.assertTrue(len(self.cart.products) == 1)
        self.assertEqual(self.cart.products[0].name, "Apple")
        print("test_add_product: Passed")
    def test_remove_product(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.remove_product("Apple")
        self.assertTrue(len(self.cart.products) == 1)
        self.assertEqual(self.cart.products[0].name, "Banana")
        print("test_remove_product: Passed")
    def test_update_quantity(self):
        self.cart.add_product(self.product1)
        self.cart.update_quantity("Apple", 10)
        self.assertEqual(self.cart.products[0].quantity, 10)
        print("test_update_quantity: Passed")
    def test_calculate_subtotal(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.assertEqual(self.cart.calculate_subtotal(), 10.0)
        print("test_calculate_subtotal: Passed")
    def test_set_tax_rate(self):
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.tax_rate, 0.08)
        print("test_set_tax_rate: Passed")
    def test_calculate_tax(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.calculate_tax(), 0.8)
        print("test_calculate_tax: Passed")
    def test_calculate_total(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.calculate_total(), 10.8)
        print("test_calculate_total: Passed")

    ## New tests
    def test_display_cart(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        with patch('builtins.print') as mocked_print:
            self.cart.display_cart()
        calls = [call(f"Name: {self.product1.name}, Price: {self.product1.price_per_unit}, Quantity: {self.product1.quantity}"),
                 call(f"Name: {self.product2.name}, Price: {self.product2.price_per_unit}, Quantity: {self.product2.quantity}")]
        mocked_print.assert_has_calls(calls)

    def test_add_existing_product(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product1)
        self.assertEqual(self.cart.products[0].quantity, 10)
        print("test_add_existing_product: Passed")

    def test_remove_nonexistent_product(self):
        self.cart.add_product(self.product1)
        initial_cart_length = len(self.cart.products)
        self.cart.remove_product("Orange")
        self.assertEqual(len(self.cart.products), initial_cart_length)
        print("test_remove_nonexistent_product: Passed")

    def test_update_quantity_nonexistent_product(self):
        self.cart.add_product(self.product1)
        initial_product_quantity = self.cart.products[0].quantity
        self.cart.update_quantity("Orange", 10)
        self.assertEqual(self.cart.products[0].quantity, initial_product_quantity)
        print("test_update_quantity_nonexistent_product: Passed")


if __name__ == "__main__":
    unittest.main()
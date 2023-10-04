from shopping_cart import ShoppingCart
from product import Product

def main():
    # Create a ShoppingCart object
    shopping_cart = ShoppingCart()
    while True:
        print("\nShopping Cart Menu")
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. Update product quantity")
        print("4. Show all items in cart")
        print("5. Calculate total cost")
        print("6. Set tax rate")
        print("7. Calculate total tax")
        print("8. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            # Add product to cart
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            shopping_cart.add_product(product)
        elif choice == '2':
            # Remove product from cart
            name = input("Enter product name: ")
            shopping_cart.remove_product(name)
        elif choice == '3':
            # Update product quantity
            name = input("Enter product name: ")
            quantity = int(input("Enter new quantity: "))
            shopping_cart.update_quantity(name, quantity)
        elif choice == '4':
            # Display all items in cart
            shopping_cart.display_cart()
        elif choice == '5':
            # Calculate and display total cost
            print("Total cost: ", shopping_cart.calculate_total())
        elif choice == '6':
            # Set tax rate
            tax_rate = float(input("Enter tax rate: "))
            shopping_cart.set_tax_rate(tax_rate)
        elif choice == '7':
            # Calculate and display total tax
            print("Total tax: ", shopping_cart.calculate_tax())
        elif choice == '8':
            print("Exiting the Shopping Cart.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
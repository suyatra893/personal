class Product:
    def __init__(self, name, quantity, price):
        self.__name = name  # Private attribute
        self.__quantity = quantity  # Private attribute
        self.__price = price  # Private attribute

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def reduce_quantity(self, quantity):
        if quantity <= self.__quantity:
            self.__quantity -= quantity
            return True
        else:
            print(f"Not enough {self.__name} in stock.")
            return False

    def __str__(self):
        return f"{self.__name} - Quantity: {self.__quantity}, Price: ${self.__price:.2f}"


class Inventory:
    def __init__(self):
        self.__products = {
            "Shoes": Product("Shoes", 200, 50.0),
            "Socks": Product("Socks", 500, 5.0),
            "T-Shirt": Product("T-Shirt", 100, 20.0),
            "Jeans": Product("Jeans", 100, 40.0),
        }

    def find_product(self, product_name):
        return self.__products.get(product_name)

    def display_inventory(self):
        print("Current Inventory:")
        for product in self.__products.values():
            print(product)

    def update_stock(self, product_name, quantity):
        product = self.find_product(product_name)
        if product:
            product.reduce_quantity(quantity)


class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, product, quantity):
        if product.get_quantity() >= quantity:
            if product.get_name() in self.__items:
                self.__items[product.get_name()]["quantity"] += quantity
            else:
                self.__items[product.get_name()] = {"product": product, "quantity": quantity}
            print(f"Added {quantity} of {product.get_name()} to the cart.")
        else:
            print(f"Cannot add {quantity} of {product.get_name()} to the cart. Not enough stock.")

    def calculate_total(self):
        total = 0
        for item in self.__items.values():
            total += item["product"].get_price() * item["quantity"]
        return total

    def display_cart(self):
        if not self.__items:
            print("Shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.__items.values():
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product.get_name()} - Quantity: {quantity}, Price: ${product.get_price() * quantity:.2f}")


class Customer:
    def __init__(self, name, shipping_address, billing_address):
        self.__name = name
        self.__shipping_address = shipping_address
        self.__billing_address = billing_address

    def get_name(self):
        return self.__name

    def get_shipping_address(self):
        return self.__shipping_address

    def get_billing_address(self):
        return self.__billing_address


class Order:
    def __init__(self, customer, shopping_cart):
        self.__customer = customer
        self.__shopping_cart = shopping_cart

    def checkout(self):
        total_amount = self.__shopping_cart.calculate_total()
        print(f"\nCheckout for {self.__customer.get_name()}:")
        print(f"Shipping Address: {self.__customer.get_shipping_address()}")
        print(f"Billing Address: {self.__customer.get_billing_address()}")
        print(f"Total Amount: ${total_amount:.2f}")


# Main Application Logic
def main():
    inventory = Inventory()
    shopping_cart = ShoppingCart()

    customer_name = input("Enter customer name: ")
    shipping_address = input("Enter shipping address: ")
    billing_address = input("Enter billing address: ")
    customer = Customer(customer_name, shipping_address, billing_address)

    while True:
        print("\nE -commerce Platform")
        print("1. Display Inventory")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory.display_inventory()

        elif choice == '2':
            product_name = input("Enter product name to add to cart: ")
            quantity = int(input("Enter quantity to add: "))
            product = inventory.find_product(product_name)
            if product:
                shopping_cart.add_item(product, quantity)
                inventory.update_stock(product_name, quantity)  # Update inventory after adding to cart
            else:
                print(f"{product_name} not found in inventory.")

        elif choice == '3':
            shopping_cart.display_cart()

        elif choice == '4':
            order = Order(customer, shopping_cart)
            order.checkout()
            break  # Exit after checkout

        elif choice == '5':
            print("Exiting the platform.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
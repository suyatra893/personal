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

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Quantity cannot be negative.")

    def reduce_quantity(self, quantity):
        if quantity <= self.__quantity:
            self.__quantity -= quantity
        else:
            print("Not enough stock available.")

    def __str__(self):
        return f"Product(Name: {self.__name}, Quantity: {self.__quantity}, Price: {self.__price})"


class Inventory:
    def __init__(self):
        self.__products = []  # Private attribute to store products

    def add_product(self, product):
        self.__products.append(product)

    def find_product(self, product_name):
        for product in self.__products:
            if product.get_name() == product_name:
                return product
        return None

    def display_inventory(self):
        if not self.__products:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product in self.__products:
                print(product)


class Customer:
    def __init__(self, name):
        self.__name = name  # Private attribute
        self.__purchased_items = {}  # Dictionary to store purchased items and their quantities

    def purchase(self, product, quantity, inventory):
        if product.get_quantity() >= quantity:
            product.reduce_quantity(quantity)
            self.__purchased_items[product.get_name()] = self.__purchased_items.get(product.get_name(), 0) + quantity
            print(f"{quantity} of {product.get_name()} purchased.")
            print("Updated Inventory after purchase:")
            inventory.display_inventory()  # Display updated inventory
        else:
            print(f"Not enough {product.get_name()} in stock to complete the purchase.")

    def calculate_total(self, inventory):
        total = 0
        for product_name, quantity in self.__purchased_items.items():
            product = inventory.find_product(product_name)
            if product:
                total += product.get_price() * quantity
        return total

    def display_purchases(self):
        if not self.__purchased_items:
            print("No items purchased.")
        else:
            print(f"{self.__name}'s Purchases:")
            for product_name, quantity in self.__purchased_items.items():
                print(f"{product_name}: {quantity}")


# Main Application Logic
def main():
    inventory = Inventory()

    # Adding some initial products to the inventory
    inventory.add_product(Product("Apple", 50, 1.0))
    inventory.add_product(Product("Banana", 30, 0.5))
    inventory.add_product(Product("Orange", 20, 0.75))

    customer_name = input("Enter customer name: ")
    customer = Customer(customer_name)

    while True:
        print("\nInventory Management System")
        print("1. Display Inventory")
        print("2. Purchase Product")
        print("3. Calculate Total Purchase Value")
        print("4. Display Purchases")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory.display_inventory()

        elif choice == '2':
            product_name = input("Enter product name to purchase: ")
            quantity = int(input("Enter quantity to purchase: "))
            product = inventory.find_product(product_name)
            if product:
                customer.purchase(product, quantity, inventory)  # Pass inventory to purchase method
            else:
                print(f"{product_name} not found in inventory.")

        elif choice == '3':
            total = customer.calculate_total(inventory)
            print(f"Total Purchase Value: ${total:.2f}")

        elif choice == '4':
            customer.display_purchases()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
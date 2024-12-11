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

    def __str__(self):
        return f"Product(Name: {self.__name}, Quantity: {self.__quantity}, Price: {self.__price})"


class Inventory:
    def __init__(self):
        self.__products = []  # Private attribute to store products

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product_name):
        for product in self.__products:
            if product.get_name() == product_name:
                self.__products.remove(product)
                print(f"{product_name} removed from inventory.")
                return
        print(f"{product_name} not found in inventory.")

    def update_product_quantity(self, product_name, quantity):
        for product in self.__products:
            if product.get_name() == product_name:
                product.set_quantity(quantity)
                print(f"Updated {product_name} quantity to {quantity}.")
                return
        print(f"{product_name} not found in inventory.")

    def display_inventory(self):
        if not self.__products:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product in self.__products:
                print(product)


# Main Application Logic
def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product Quantity")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = int(input("Enter product price in Dollars1: "))
            product = Product(name, quantity, price)
            inventory.add_product(product)
            print(f"{name} added to inventory.")

        elif choice == '2':
            name = input("Enter product name to remove: ")
            inventory.remove_product(name)

        elif choice == '3':
            name = input("Enter product name to update quantity: ")
            quantity = int(input("Enter new quantity: "))
            inventory.update_product_quantity(name, quantity)

        elif choice == '4':
            inventory.display_inventory()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
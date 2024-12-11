class Account:
    def __init__(self):
        self.acc_name = ""
        self.acc_number = 0
        self.acc_balance = 0

    def getdata(self):
        self.acc_name = input("Enter the name of the customer: ")
        self.acc_number = int(input("Enter the account number of the customer: "))
        self.acc_balance = float(input("Enter the account balance of the customer: "))

    def deposit(self):
        deposit = float(input("Enter the amount you want to deposit: "))
        self.acc_balance += deposit
        print(f"New balance after deposit: ${self.acc_balance:.2f}")
        return self.acc_balance

    def withdrawal(self):
        withdrawal = float(input("Enter the amount you want to withdraw: "))
        if withdrawal > self.acc_balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.acc_balance -= withdrawal
            print(f"New balance after withdrawal: ${self.acc_balance:.2f}")
        return self.acc_balance

    def display(self):
        print(f"Account Name: {self.acc_name}")
        print(f"Account Number: {self.acc_number}")
        print(f"Account Balance: ${self.acc_balance:.2f}")


def main():
    accounts = []  # List to store multiple accounts

    while True:
        print("\nBank Account Management System")
        print("1. Create a new account")
        print("2. Manage existing account")
        print("3. Display all accounts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc = Account()
            acc.getdata()
            accounts.append(acc)  # Add the new account to the list
            print("Account created successfully.")

        elif choice == '2':
            if not accounts:
                print("No accounts available. Please create an account first.")
                continue

            acc_number = int(input("Enter the account number to manage: "))
            found = False
            for acc in accounts:
                if acc.acc_number == acc_number:
                    found = True
                    while True:
                        print("\nAccount Management Menu")
                        print("1. Deposit")
                        print("2. Withdrawal")
                        print("3. Display Account Details")
                        print("4. Go Back")
                        action = input("Enter your choice: ")

                        if action == '1':
                            acc.deposit()
                        elif action == '2':
                            acc.withdrawal()
                        elif action == '3':
                            acc.display()
                        elif action == '4':
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    break
            if not found:
                print("Account not found.")

        elif choice == '3':
            if not accounts:
                print("No accounts available.")
            else:
                print("\nAll Accounts:")
                for acc in accounts:
                    acc.display()

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
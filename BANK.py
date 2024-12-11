accounts = []
customer_id = 1

while True:
    # Display menu options
    print("\nBank Management System")
    print("1. Open a savings bank account")
    print("2. Add a customer")
    print("3. Deposit money")
    print("4. Display sorted records")
    print("5. Close/delete account")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    # Option 1: Open a savings bank account
    if choice == 1:
        name = input("Enter customer name: ")
        balance = float(input("Enter initial balance: "))
        

        account_number = int(input("enter the account number: "))
        
        account = {
            'customer_id': customer_id,
            'name': name,
            'balance': balance,
            'account_number': account_number
        }
        accounts.append(account)
        
        print(f"Account created successfully with Customer ID: {customer_id} and Account Number: {account_number}")
        customer_id += 1

    # Option 2: Add a customer
    elif choice == 2:
        name = input("Enter customer name: ")
        balance = float(input("Enter initial balance: "))
        
        # Generate a 16-digit account number
        account_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
        
        account = {
            'customer_id': customer_id,
            'name': name,
            'balance': balance,
            'account_number': account_number
        }
        accounts.append(account)
        
        print(f"Customer added successfully with Customer ID: {customer_id} and Account Number: {account_number}")
        customer_id += 1

    # Option 3: Deposit money
    elif choice == 3:
        cust_id = int(input("Enter Customer ID: "))
        found = False
        for account in accounts:
            if account['customer_id'] == cust_id:
                amount = float(input("Enter amount to deposit: "))
                account['balance'] += amount
                print(f"Deposit successful! New balance: {account['balance']}")
                found = True
                break
        if not found:
            print("Account not found!")

    # Option 4: Display sorted records
    elif choice == 4:
        if accounts:
            sorted_accounts = sorted(accounts, key=lambda x: x['name'])
            print("Customer ID | Account Number | Name | Balance")
            for account in sorted_accounts:
                print(f"{account['customer_id']} | {account['account_number']} | {account['name']} | {account['balance']}")
        else:
            print("No accounts to display.")

    # Option 5: Close/delete account
    elif choice == 5:
        cust_id = int(input("Enter Customer ID to delete: "))
        found = False
        for i in range(len(accounts)):
            if accounts[i]['customer_id'] == cust_id:
                print(f"Deleting Account Number: {accounts[i]['account_number']}")
                accounts.pop(i)
                print("Account deleted successfully.")
                found = True
                break
        if not found:
            print("Account not found!")

    # Option 6: Exit
    elif choice == 6:
        print("Exiting the system.")
        break

    else:
        print("Invalid choice! Please try again.")

# ATM Simulation

# Default starting balance and PIN
account_balance = 1000
pin = "1234"
transaction_history = []

def check_pin(input_pin):
    """Checks if the entered PIN is correct"""
    return input_pin == pin

def balance_inquiry():
    """Displays the current balance"""
    print(f"Your current balance is: ${account_balance}")
    transaction_history.append("Balance Inquiry")

def cash_withdrawal():
    """Handles cash withdrawal"""
    global account_balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= account_balance:
        account_balance -= amount
        print(f"Withdrawal successful! You withdrew: ${amount}")
        transaction_history.append(f"Withdrawal of ${amount}")
    else:
        print("Insufficient funds!")
        transaction_history.append("Failed withdrawal attempt")

def cash_deposit():
    """Handles cash deposit"""
    global account_balance
    amount = float(input("Enter the amount to deposit: "))
    account_balance += amount
    print(f"Deposit successful! You deposited: ${amount}")
    transaction_history.append(f"Deposit of ${amount}")

def change_pin():
    """Allows the user to change their PIN"""
    global pin
    new_pin = input("Enter your new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        pin = new_pin
        print("PIN successfully changed!")
        transaction_history.append("PIN Change")
    else:
        print("Invalid PIN format! Please try again.")

def view_transaction_history():
    """Displays the transaction history"""
    if transaction_history:
        print("Transaction History:")
        for transaction in transaction_history:
            print(transaction)
    else:
        print("No transactions yet.")

def atm_operations():
    """Main ATM operation menu"""
    print("Welcome to the ATM!")
    entered_pin = input("Please enter your 4-digit PIN: ")

    if check_pin(entered_pin):
        while True:
            print("\nATM Menu:")
            print("1. Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")

            choice = input("Please select an option (1-6): ")

            if choice == '1':
                balance_inquiry()
            elif choice == '2':
                cash_withdrawal()
            elif choice == '3':
                cash_deposit()
            elif choice == '4':
                change_pin()
            elif choice == '5':
                view_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")
    else:
        print("Incorrect PIN. Access denied.")

# Run the ATM simulation
atm_operations()

balance = 0
transaction_history = []
correct_pin = "220806"
attempts = 3                    
print("-----------------welcome to the bank-----------------")
while attempts > 0:
    entered_pin = input("Please enter your PIN: ")
    if entered_pin == correct_pin:
        print("PIN accepted. You can now access your account.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempt(s) left.")  
else:
    print("Too many incorrect attempts. Exiting the system.")
    exit()
while True:
    print("\nSelect an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")             
    if choice == '1':
        print(f"Your current balance is: ${balance}")
    elif choice == '2':
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive value.")
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: $"))
        if 0 < amount <= balance:
            balance -= amount
            transaction_history.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid amount. Please check your balance and try again.")
    elif choice == '4':
        if transaction_history:
            print("Transaction History:")
            for transaction in transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")
    elif choice == '5':
        print("Thank you for banking with us. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")
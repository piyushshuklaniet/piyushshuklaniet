def initialize_account():
    return 5000, 1234

def check_balance(balance):

    print(f"Current Balance: Rs.{balance}")

def withdraw_cash(balance, amount):
  
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. Remaining Balance: ${balance}")
    else:
        print("Invalid amount or insufficient funds.")

    return balance

def deposit_cash(balance, amount):
   
    if amount > 0:
        balance += amount
        print(f"Deposit successful. New Balance: ${balance}")
    else:
        print("Invalid deposit amount.")

    return balance

# Main function to run the banking operations
def main():
    # Initialize a Bank Account
    balance, pin = initialize_account()

    # Continuous loop until the user decides to exit
    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: $"))
            balance = withdraw_cash(balance, amount)
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: $"))
            balance = deposit_cash(balance, amount)
        elif choice == "4":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main function if the script is executed
if __name__ == "_main_":
    main()
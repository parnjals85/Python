balance = 1000
while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Balance")
    print("3. Withdraw Balance")
    print("4. Exit")

    choice = input("Please enter the choice (1-4): ")

    if choice == "1":
        print(f"💰 Your Balance is ₹{balance}")

    elif choice == "2":
        amount = int(input("Enter the amount you want to deposit: "))
        balance += amount
        print(f"₹{amount} deposited successfully")
        print(f"Now Total Balance is {balance}")

    elif choice == "3":
        amount = int(input("Enter the amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid choice, please try again")

   

accounts = [
    {
        "name": "John Smith",
        "balance": 20000,
        "overdraft": 5000,
        "username": "johnsmith",
        "password": "1234"
    },
    {
        "name": "David Johnson",
        "balance": 40000,
        "overdraft": 10000,
        "username": "davidjohnson",
        "password": "5678"
    },
    {
        "name": "Emily Clark",
        "balance": 85000,
        "overdraft": 35000,
        "username": "emilyclark",
        "password": "3456"
    }
]

def register():
    print("\nRegistration Screen")
    name = input("Full Name: ")
    username = input("Username: ")
    password = input("Password: ")

    for acc in accounts:
        if acc["username"] == username:
            print("This username already exists.")
            return

    new_account = {
        "name": name,
        "username": username,
        "password": password,
        "balance": 0,
        "overdraft": 10000
    }
    accounts.append(new_account)
    print("Registration successful. You can now log in.")

import sys
def login():
    attempts = 3
    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        is_logged_in = False
        for account in accounts:
            if username == account["username"] and account["password"] == password:
                is_logged_in = True
                print("Login successful. Welcome " + account["name"])
                menu(account)
                return
        if not is_logged_in:
            print("Login failed. Please check your credentials.")
        attempts -= 1
        print(f"Login failed. Remaining attempts: {attempts}")
    print("Too many incorrect attempts. You have been logged out.")
    sys.exit()

def menu(account):
    choice = 0
    while choice != 4:
        try:
            choice = int(input("\n1-Withdraw Money\n2-Deposit Money\n3-Check Balance\n4-Logout\nChoose an option: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if choice == 1:
            withdraw_money(account)
        elif choice == 2:
            deposit_money(account)
        elif choice == 3:
            check_balance(account)
        elif choice == 4:
            print("Logging out...")
            break
        else:
            print("Invalid option!")

def withdraw_money(account):
    try:
        amount = int(input("Enter the amount you want to withdraw: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if account["balance"] >= amount:
        account["balance"] -= amount
        print("Withdrawal successful.")
    else:
        try:
            use_overdraft = int(input("Insufficient balance! Use overdraft account? (1: yes, 2: no): "))
        except ValueError:
            print("Invalid choice.")
            return
        if use_overdraft == 1:
            if account["balance"] + account["overdraft"] >= amount:
                amount -= account["balance"]
                account["balance"] = 0
                account["overdraft"] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient total funds.")
        else:
            print("Withdrawal canceled.")

def check_balance(account):
    print(f"Your balance: {account['balance']} TL")
    print(f"Your overdraft balance: {account['overdraft']} TL")

def deposit_money(account):
    try:
        amount = int(input("Enter the amount you want to deposit: "))
        account["balance"] += amount
        print("Deposit successful.")
    except ValueError:
        print("Please enter a valid number!")

def start():
    while True:
        print("\n=== BANKING SYSTEM ===")
        choice = input("1- Login\n2- Register\n3- Exit\nYour choice: ")
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.")

start()

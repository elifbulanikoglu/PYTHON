def signUp():
    username = input("Username: ")
    with open("users.txt", "r", encoding = 'utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 4 and parts[1] == username:
                print("\nThis username is already taken! Please enter another username.\n")
                return
            
    password = input("Password: ")
    print("\nRegistration successful.\n")
    with open("users.txt", "a", encoding = 'utf-8') as file:
        file.write(f"Username {username} password {password}\n")

def logIn():
    username = input("\nUsername: ")
    password = input("Password: ")
    found = False
    with open("users.txt", "r", encoding = 'utf-8') as data:
        for line in data:
            if line.strip() == f"Username {username} password {password}":
                print("\nLogin successful.\n")
                found = True
                break
    if not found:
            print("\nInvalid username or password.\n")

def menu():
    while True:
            choice = input("  == USER SYSTEM ==  \n1- Sign up\n2- Log in\n3- Exit\nYour choice:  ")
            if choice == "1":
                signUp()
            elif choice == "2":
                logIn()
            elif choice == "3":
                print("\nExiting program...")
                break
            else:
                print("\n\nInvalid choice! Please enter 1, 2 or 3.\n")

menu()
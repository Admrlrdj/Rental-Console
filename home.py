from auth import login, register

def home():
    print("=============== Welcome ===============")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Please try again.")
        home()

home()
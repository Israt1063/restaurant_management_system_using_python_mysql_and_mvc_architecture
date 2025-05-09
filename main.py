1
from view.cli import CLI

def main():
    cli = CLI()
    while True:
        print("\nRestaurant Management System")
        print("1. Show Menu")
        print("2. Create Order")
        print("3. Generate Bill")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            cli.show_menu()
        elif choice == "2":
            cli.create_order()
        elif choice == "3":
            cli.generate_bill()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

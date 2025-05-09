from controller.app_controller import AppController

class CLI:
    def __init__(self):
        self.controller = AppController()

    def show_menu(self):
        menu_items = self.controller.menu.get_menu()
        for item in menu_items:
            print(f"{item[0]} - {item[1]} (${item[2]})")

    def create_order(self):
        user_id = input("Enter User ID: ")
        menu_items = input("Enter Menu Items: ")
        total_amount = float(input("Enter Total Amount: "))
        self.controller.create_order(user_id, menu_items, total_amount)
        print("Order placed successfully!")

    def generate_bill(self):
        order_id = input("Enter Order ID: ")
        bill = self.controller.generate_bill(order_id)
        print(f"Bill Details: {bill}")

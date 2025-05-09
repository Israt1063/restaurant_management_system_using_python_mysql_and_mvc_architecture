from model.menu import Menu
from model.order import Order
from model.user import User
from model.bill import Bill

class AppController:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()
        self.user = User()
        self.bill = Bill()

    def create_order(self, user_id, menu_items, total_amount):
        self.order.create_order(user_id, menu_items, total_amount)

    def generate_bill(self, order_id):
        return self.bill.generate_bill(order_id)

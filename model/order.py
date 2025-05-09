from model.database import Database

class Order:
    def __init__(self):
        self.db = Database()

    def create_order(self, user_id, menu_items, total_amount):
        query = "INSERT INTO orders (user_id, menu_items, total_amount) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (user_id, menu_items, total_amount))

    def get_orders(self):
        query = "SELECT * FROM orders"
        return self.db.fetch_data(query)

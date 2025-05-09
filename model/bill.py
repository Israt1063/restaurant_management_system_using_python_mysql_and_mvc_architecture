#bill.py
from model.database import Database

class Bill:
    def __init__(self):
        self.db = Database()

    def generate_bill(self, order_id):
        query = "SELECT * FROM orders WHERE id = %s"
        order = self.db.fetch_data(query, (order_id,))
        return order

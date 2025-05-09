from model.database import Database

class Menu:
    def __init__(self):
        self.db = Database()

    def add_menu_item(self, name, price, category):
        query = "INSERT INTO menu (name, price, category) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (name, price, category))

    def get_menu(self):
        query = "SELECT * FROM menu"
        return self.db.fetch_data(query)

    def delete_menu_item(self, item_id):
        query = "DELETE FROM menu WHERE id = %s"
        self.db.execute_query(query, (item_id,))

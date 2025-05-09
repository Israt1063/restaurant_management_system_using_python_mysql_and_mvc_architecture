from model.database import Database

class User:
    def __init__(self):
        self.db = Database()

    def add_user(self, name, role):
        query = "INSERT INTO users (name, role) VALUES (%s, %s)"
        self.db.execute_query(query, (name, role))

    def get_users(self):
        query = "SELECT * FROM users"
        return self.db.fetch_data(query)

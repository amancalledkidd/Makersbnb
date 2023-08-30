from lib.user import User


class UserRepository:
    def __init__(self, db_connection) -> None:
        self._connection = db_connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"],
                        row["password"], row["phone_number"])
            users.append(item)
        return users

    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (name, email, password, phone_number) VALUES (%s, %s, %s, %s) RETURNING id', [
                                        user.name, user.email, user.password, user.phone_number])
        row = rows[0]
        user.id = row['id']
        return user

    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"],
                    row["password"], row["phone_number"])
    
    def find_by_email(self, user_email):
        rows = self._connection.execute(
            'SELECT * from users WHERE email = %s', [user_email])
        row = rows[0]
        return User(row["id"], row["name"], row["email"],
                    row["password"], row["phone_number"])
    
    # def check_email_and_password(self, email, password):
    #     user = self.find_by_email(email)
    #     return user.password == password
            
        

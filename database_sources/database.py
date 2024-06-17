import sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_connection(self):
        return sqlite3.connect(self.database_name, check_same_thread=False)

    def create_table(self):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS USERS
                (LOGIN TEXT PRIMARY KEY,
                EMAIL TEXT,
                PASSWORD TEXT);
            """)
            conn.commit()

    def find_user(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT LOGIN FROM USERS WHERE LOGIN = '{login}'")
            user = cursor.fetchone()
            return user

    def find_user_password(self, login, password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT LOGIN, PASSWORD FROM USERS WHERE LOGIN = ? AND PASSWORD = ?",
                (login, password))
            user = cursor.fetchone()
            return user

    def find_user_email(self, email):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT EMAIL FROM USERS WHERE EMAIL = '{email}'")
            user = cursor.fetchone()
            return user

    def add_user(self, login, email, password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO USERS (LOGIN, EMAIL, PASSWORD) VALUES (?, ?, ?)",
                (login, email, password)
            )
            conn.commit()

    def get_users(self):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM USERS")
            return cursor.fetchall()

import sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_connection(self):
        return sqlite3.connect(self.database_name, check_same_thread=False)

    def create_table_users(self):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS USERS
                (LOGIN TEXT PRIMARY KEY,
                EMAIL TEXT,
                PASSWORD TEXT);
            """)
            conn.commit()

    def create_table_theory(self):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS THEORY (
                    USER_LOGIN TEXT PRIMARY KEY,
                    THEORY_1 BOOLEAN DEFAULT False,
                    THEORY_2 BOOLEAN DEFAULT False,
                    THEORY_3 BOOLEAN DEFAULT False,
                    THEORY_4 BOOLEAN DEFAULT False,
                    THEORY_5 BOOLEAN DEFAULT False,
                    THEORY_6 BOOLEAN DEFAULT False,
                    THEORY_7 BOOLEAN DEFAULT False,
                    THEORY_8 BOOLEAN DEFAULT False,
                    FOREIGN KEY (USER_LOGIN) REFERENCES USERS(LOGIN)
                );
            """)
            conn.commit()

    def create_table_test(self):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS TESTS (
                    USER_LOGIN TEXT PRIMARY KEY,
                    TESTS_1 INT DEFAULT 0,
                    TESTS_2 INT DEFAULT 0,
                    TESTS_3 INT DEFAULT 0,
                    TESTS_4 INT DEFAULT 0,
                    TESTS_5 INT DEFAULT 0,
                    TESTS_6 INT DEFAULT 0,
                    TESTS_7 INT DEFAULT 0,
                    TESTS_8 INT DEFAULT 0,
                    FOREIGN KEY (USER_LOGIN) REFERENCES USERS(LOGIN)
                );
            """)
            conn.commit()

    def create_table_practice(self):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS PRACTICE (
                    USER_LOGIN TEXT PRIMARY KEY,
                    PRACTICE_1 BOOLEAN DEFAULT False,
                    FOREIGN KEY (USER_LOGIN) REFERENCES USERS(LOGIN)
                );
            """)
            conn.commit()

    def add_user(self, login, email, password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            "INSERT INTO USERS (LOGIN, EMAIL, PASSWORD) "
                "VALUES (?, ?, ?)",
                (login, email, password)
            )
            conn.commit()

    def find_user_login(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT LOGIN FROM USERS WHERE LOGIN = '{login}'")
            user = cursor.fetchone()
            return user

    def find_user_password(self, login, password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT LOGIN, PASSWORD FROM USERS "
                "WHERE LOGIN = ? AND PASSWORD = ?",
                (login, password))
            user = cursor.fetchone()
            return user

    def find_user_email(self, email):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT EMAIL FROM USERS WHERE EMAIL = '{email}'")
            user = cursor.fetchone()
            return user

    def find_user_password_by_email(self, email, password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT EMAIL, PASSWORD FROM USERS WHERE EMAIL = ? AND "
                "PASSWORD = ?",
                (email, password)
            )
            user = cursor.fetchone()
            return user

    def find_login_by_email(self, email):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT LOGIN FROM USERS WHERE EMAIL = '{email}'"
            )
            user = cursor.fetchone()
            return user

    def add_new_theory(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO THEORY (USER_LOGIN) VALUES (?)",
                (login,)
            )
            conn.commit()

    def add_new_tests(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO TESTS (USER_LOGIN) VALUES (?)",
                (login,)
            )
            conn.commit()

    def add_new_practice(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO PRACTICE (USER_LOGIN) VALUES (?)",
                (login,)
            )
            conn.commit()

    def get_completed_theory_count(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT SUM(
                    CASE WHEN THEORY_1 = 1 THEN 1 ELSE 0 END +
                    CASE WHEN THEORY_2 = 1 THEN 1 ELSE 0 END +
                    CASE WHEN THEORY_3 = 1 THEN 1 ELSE 0 END +
                    CASE WHEN THEORY_4 = 1 THEN 1 ELSE 0 END +
                    CASE WHEN THEORY_5 = 1 THEN 1 ELSE 0 END +
                    CASE WHEN THEORY_6 = 1 THEN 1 ELSE 0 END +
                    CASE WHEN THEORY_7 = 1 THEN 1 ELSE 0 END +
                    CASE WHEN THEORY_8 = 1 THEN 1 ELSE 0 END
                ) AS completed_theory_count
                FROM THEORY
                WHERE USER_LOGIN = ?
            """, (login,))
            completed_theory_count = cursor.fetchone()[0]
            return completed_theory_count

    def get_completed_practice_count(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT SUM(
                    CASE WHEN PRACTICE_1 = 1 THEN 1 ELSE 0 END +
                ) AS completed_theory_count
                FROM THEORY
                WHERE USER_LOGIN = ?
            """, (login,))
            completed_theory_count = cursor.fetchone()[0]
            return completed_theory_count

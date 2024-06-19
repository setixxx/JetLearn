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

    def check_user_login(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT LOGIN FROM USERS "
                "WHERE LOWER(LOGIN) = LOWER(?)",
                (login,)
           )
            user = cursor.fetchone()
            return user

    def check_user_email(self, email):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT EMAIL FROM USERS "
                "WHERE LOWER(EMAIL) = LOWER(?)",
                (email,)
            )
            user = cursor.fetchone()
            return user

    def check_user_password(self, login, password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT LOGIN, PASSWORD FROM USERS "
                "WHERE LOGIN = ? AND PASSWORD = ?",
                (login, password))
            user = cursor.fetchone()
            return user

    def find_user_and_password_by_email(self, email, password):
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

    def find_email_by_login(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT EMAIL FROM USERS WHERE LOGIN = ?",
                (login,)
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

            # Получаем список столбцов в таблице PRACTICE, кроме USER_LOGIN
            cursor.execute("PRAGMA table_info(PRACTICE)")
            columns = [col[1] for col in cursor.fetchall() if
                       col[1] != 'USER_LOGIN']

            # Формируем динамический SQL-запрос для подсчета количества True
            conditions_true = [f"CASE WHEN {col} = 1 THEN 1 ELSE 0 END" for col
                               in columns]
            query_true = f"""
                SELECT SUM({' + '.join(conditions_true)}) 
                AS completed_practice_count
                FROM PRACTICE
                WHERE USER_LOGIN = ?
            """

            # Формируем динамический SQL-запрос для подсчета общего
            # количества практических заданий
            conditions_total = [
                f"CASE WHEN {col} IS NOT NULL THEN 1 ELSE 0 END" for col in
                columns]
            query_total = f"""
                SELECT SUM({' + '.join(conditions_total)}) 
                AS total_practice_count
                FROM PRACTICE
                WHERE USER_LOGIN = ?
            """

            # Выполняем запросы
            cursor.execute(query_true, (login,))
            completed_practice_count = cursor.fetchone()[0]

            cursor.execute(query_total, (login,))
            total_practice_count = cursor.fetchone()[0]

            return completed_practice_count, total_practice_count

    def update_user_login(self, old_login, new_login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            # Обновляем логин в таблице USERS
            cursor.execute(
                "UPDATE USERS SET LOGIN = ? WHERE LOGIN = ?",
                (new_login, old_login)
            )
            # Обновляем логин в таблице THEORY
            cursor.execute(
                "UPDATE THEORY SET USER_LOGIN = ? WHERE USER_LOGIN = ?",
                (new_login, old_login)
            )
            # Обновляем логин в таблице TESTS
            cursor.execute(
                "UPDATE TESTS SET USER_LOGIN = ? WHERE USER_LOGIN = ?",
                (new_login, old_login)
            )
            # Обновляем логин в таблице PRACTICE
            cursor.execute(
                "UPDATE PRACTICE SET USER_LOGIN = ? WHERE USER_LOGIN = ?",
                (new_login, old_login)
            )
            conn.commit()

    def update_user_email(self, login, new_email):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE USERS SET EMAIL = ? WHERE LOGIN = ?",
                (new_email, login)
            )
            conn.commit()

    def update_user_password(self, login, new_password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE USERS SET PASSWORD = ? WHERE LOGIN = ?",
                (new_password, login)
            )
            conn.commit()

    def get_test_results_and_grades(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT TESTS_1, TESTS_2, TESTS_3, TESTS_4, TESTS_5, 
                TESTS_6, TESTS_7, TESTS_8
                FROM TESTS
                WHERE USER_LOGIN = ?
            """, (login,))
            results = cursor.fetchone()

            grades = []
            for result in results:
                if result in (1, 2):
                    grades.append(2)
                elif result == 3:
                    grades.append(3)
                elif result == 4:
                    grades.append(4)
                elif result == 5:
                    grades.append(5)
                else:
                    grades.append(
                        2)  # Default grade if result is 0 or undefined

            return results, grades

    def get_completed_tests_count(self, login):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT TESTS_1, TESTS_2, TESTS_3, TESTS_4, TESTS_5, 
                TESTS_6, TESTS_7, TESTS_8
                FROM TESTS
                WHERE USER_LOGIN = ?
            """, (login,))
            results = cursor.fetchone()

            if results is None:
                return 0

            completed_tests_count = sum(1 for result in results if result > 0)
            return completed_tests_count

    def update_theory(self, login, column, value):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            query = f"UPDATE THEORY SET {column} = ? WHERE USER_LOGIN = ?"
            cursor.execute(query, (value, login))
            conn.commit()

    def update_tests(self, login, column, value):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            query = f"UPDATE TESTS SET {column} = ? WHERE USER_LOGIN = ?"
            cursor.execute(query, (value, login))
            conn.commit()
            
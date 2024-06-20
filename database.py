import sqlite3

class DatabaseManager:
    # Класс для управления базой данных.
    def __init__(self, database_name):
        # Инициализирует имя базы данных.
        self.database_name = database_name

    def create_connection(self):
        # Создает соединение с базой данных.
        return sqlite3.connect(self.database_name, check_same_thread=False)

    def create_table_users(self):
        # Создает таблицу пользователей.
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
        # Создает таблицу для хранения данных о теории.
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
        # Создает таблицу для хранения результатов тестов.
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
        # Создает таблицу для хранения статистики практических заданий.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS PRACTICE (
                    USER_LOGIN TEXT PRIMARY KEY,
                    CORRECT_ATTEMPTS INT DEFAULT 0,
                    TOTAL_ATTEMPTS INT DEFAULT 0,
                    FOREIGN KEY (USER_LOGIN) REFERENCES USERS(LOGIN)
                );
            """)
            conn.commit()

    def add_user(self, login, email, password):
        # Добавляет нового пользователя в таблицу.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            "INSERT INTO USERS (LOGIN, EMAIL, PASSWORD) "
                "VALUES (?, ?, ?)",
                (login, email, password)
            )
            conn.commit()

    def check_user_login(self, login):
        # Проверяет наличие пользователя по логину.
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
        # Проверяет наличие пользователя по email.
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
        # Проверяет пароль пользователя.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT LOGIN, PASSWORD FROM USERS "
                "WHERE LOGIN = ? AND PASSWORD = ?",
                (login, password))
            user = cursor.fetchone()
            return user

    def find_user_and_password_by_email(self, email, password):
        # Находит пользователя по email и паролю.
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
        # Находит логин по email.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT LOGIN FROM USERS WHERE EMAIL = '{email}'"
            )
            user = cursor.fetchone()
            return user

    def find_email_by_login(self, login):
        # Находит email по логину.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT EMAIL FROM USERS WHERE LOGIN = ?",
                (login,)
            )
            user = cursor.fetchone()
            return user

    def add_new_theory(self, login):
        # Добавляет новую запись о теории для пользователя.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO THEORY (USER_LOGIN) VALUES (?)",
                (login,)
            )
            conn.commit()

    def add_new_tests(self, login):
        # Добавляет новую запись о тестах для пользователя.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO TESTS (USER_LOGIN) VALUES (?)",
                (login,)
            )
            conn.commit()

    def add_new_practice(self, login):
        # Добавляет новую запись о практических заданиях для пользователя.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO PRACTICE (USER_LOGIN) VALUES (?)",
                (login,)
            )
            conn.commit()

    def get_completed_theory_count(self, login):
        # Возвращает количество пройденных модулей теории.
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

    def update_user_login(self, old_login, new_login):
        # Обновляет логин пользователя.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            # Обновляем логин в таблице USERS
            cursor.execute(
                "UPDATE USERS SET LOGIN = ? WHERE LOGIN = ?",
                (new_login, old_login)
            )
            conn.commit()

    def update_user_email(self, login, new_email):
        # Обновляет email пользователя.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE USERS SET EMAIL = ? WHERE LOGIN = ?",
                (new_email, login)
            )
            conn.commit()

    def update_user_password(self, login, new_password):
        # Обновляет пароль пользователя.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE USERS SET PASSWORD = ? WHERE LOGIN = ?",
                (new_password, login)
            )
            conn.commit()

    def get_test_results_and_grades(self, login):
        # Получает результаты тестов и оценки.
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
                        "Нет")

            return results, grades

    def get_completed_tests_count(self, login):
        # Возвращает количество пройденных тестов.
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
        # Обновляет данные о теории.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            query = f"UPDATE THEORY SET {column} = ? WHERE USER_LOGIN = ?"
            cursor.execute(query, (value, login))
            conn.commit()

    def update_tests(self, login, column, value):
        # Обновляет результаты тестов.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            query = f"UPDATE TESTS SET {column} = ? WHERE USER_LOGIN = ?"
            cursor.execute(query, (value, login))
            conn.commit()

    def increment_correct_attempts(self, login):
        # Увеличивает количество правильных ответов.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE PRACTICE SET "
                "CORRECT_ATTEMPTS = CORRECT_ATTEMPTS + 1 "
                "WHERE USER_LOGIN = ?",
                (login,)
            )
            conn.commit()

    def increment_total_attempts(self, login):
        # Увеличивает общее количество попыток.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE PRACTICE "
                "SET TOTAL_ATTEMPTS = TOTAL_ATTEMPTS + 1 "
                "WHERE USER_LOGIN = ?",
                (login,)
            )
            conn.commit()

    def get_practice_stats(self, login):
        # Получает статистику по практическим заданиям.
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT CORRECT_ATTEMPTS, TOTAL_ATTEMPTS
                FROM PRACTICE
                WHERE USER_LOGIN = ?
            """, (login,))
            stats = cursor.fetchone()
            return stats if stats else (0, 0)
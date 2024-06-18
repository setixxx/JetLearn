class AppState:
    def __init__(self):
        self.user_login = None
        self.user_email = None
        self.password = None
        self.completed_theory = None
        self.completed_practice_count = None
        self.completed_practice_total = None
        self.completed_tests = None

    def set_login(self, login):
        self.user_login = login

    def get_login(self):
        return self.user_login

    def set_email(self, email):
        self.user_email = email

    def get_email(self):
        return self.user_email

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_completed_theory(self, completed_theory):
        self.completed_theory = completed_theory

    def get_completed_theory(self):
        return self.completed_theory / 8

    def get_formatted_theory(self):
        return f"{self.completed_theory} из 8"

    def get_formatted_theory_backslash(self):
        return f"{self.completed_theory} / 8"

    def set_completed_tests(self, completed_tests):
        self.completed_tests = completed_tests

    def get_completed_tests(self):
        return self.completed_tests / 8

    def get_formatted_tests(self):
        return f"{self.completed_tests} из 8"

    def set_completed_practice_count(self, completed_practice):
        self.completed_practice_count = completed_practice

    def set_completed_practice_total(self, completed_practice):
        self.completed_practice_total = completed_practice

    def get_formatted_practice(self):
        return (f"{self.completed_practice_count} / "
                f"{self.completed_practice_total}")

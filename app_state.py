class AppState:
    def __init__(self):
        self.user_login = None
        self.completed_theory = None

    def set_login(self, login):
        self.user_login = login

    def get_login(self):
        return self.user_login

    def set_completed_theory(self, completed_theory):
        self.completed_theory = completed_theory

    def get_completed_theory(self):
        return self.completed_theory/8

    def get_formatted_theory(self):
        return f"{self.completed_theory} из 8"

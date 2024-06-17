class AppState:
    def __init__(self):
        self.user_login = None

    def set_login(self, login):
        self.user_login = login

    def get_login(self):
        return self.user_login

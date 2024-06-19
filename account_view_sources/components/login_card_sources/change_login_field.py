import flet as ft


class ChangeLoginField(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 344
        self.height = 114
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(top=16,
                                       left=32)
        self.login_change_field = ft.TextField(
            label="Новый логин",
            text_size=16,
            width=280,
            max_length=16,
        )
        self.content = self.login_change_field

    def get_login_change_field(self):
        return self.login_change_field.value

    def get_login_change_error_text(self):
        return self.login_change_field.error_text

    def set_login_error_change(self, error_text):
        self.login_change_field.error_text = error_text
        self.login_change_field.update()

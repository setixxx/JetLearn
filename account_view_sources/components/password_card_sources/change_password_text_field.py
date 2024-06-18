import flet as ft

class ChangePasswordField(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 344
        self.height = 228
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(top=16,
                                       left=32)
        self.old_password_change_field = ft.TextField(
            label="Старый пароль",
            text_size=16,
            width=280,
            max_length=16,
        )
        self.new_password_change_field = ft.TextField(
            label="Новый пароль",
            text_size=16,
            width=280,
            max_length=16,
        )
        self.content = ft.Column(
            [
                self.old_password_change_field,
                self.new_password_change_field
            ],
        )

    def get_old_password_change_field(self):
        return self.old_password_change_field.value

    def get_new_password_change_field(self):
        return self.new_password_change_field.value

    def get_old_password_change_error_text(self):
        return self.old_password_change_field.error_text

    def get_new_password_change_error_text(self):
        return self.new_password_change_field.error_text

    def set_old_password_error_change(self, error_text):
        self.old_password_change_field.error_text = error_text
        self.old_password_change_field.update()

    def set_new_password_error_change(self, error_text):
        self.new_password_change_field.error_text = error_text
        self.new_password_change_field.update()

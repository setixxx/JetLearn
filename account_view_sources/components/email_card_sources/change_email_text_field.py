import flet as ft


class ChangeEmailField(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 344
        self.height = 114
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(top=16,
                                       left=32)
        self.email_change_field = ft.TextField(
            label="Адрес эл. почты",
            text_size=16,
            width=280,
            max_length=36,
        )
        self.content = self.email_change_field

    def get_email_change_field(self):
        return self.email_change_field.value

    def get_email_change_error_text(self):
        return self.email_change_field.error_text

    def set_email_error_change(self, error_text):
        self.email_change_field.error_text = error_text
        self.email_change_field.update()

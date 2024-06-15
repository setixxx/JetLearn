import flet as ft

class Subheader(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(left=22, top=3)
        self.width = 344
        self.height = 124
        self.content = ft.Row(
            [
                ft.Text(
                    "Информация о вашем аккаунте.\n"
                    "По желанию вы можете ее изменить.\n"
                    "Не забывайте обновлять эту информацию,\n"
                    "чтобы у вас всегда был доступ к аккаунту\n"
                    "JetLearn",
                    size=14,
                    weight=ft.FontWeight.W_500,
                    style=ft.TextStyle(
                        height=1.2
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START
        )
import flet as ft

# Класс для представления виджета подзаголовка
class Subheader(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка отступов слева и сверху
        self.padding = ft.padding.only(left=22, top=3)
        # Установка ширины виджета
        self.width = 344
        # Установка высоты виджета
        self.height = 124
        # Создание строки с текстом подзаголовка
        self.content = ft.Row(
            [
                # Виджет текста подзаголовка
                ft.Text(
                    # Текст подзаголовка
                    "Информация о вашем аккаунте.\n"
                    "По желанию вы можете ее изменить.\n"
                    "Не забывайте обновлять эту информацию,\n"
                    "чтобы у вас всегда был доступ к аккаунту\n"
                    "JetLearn",
                    # Размер текста
                    size=14,
                    # Вес шрифта
                    weight=ft.FontWeight.W_500,
                    # Стиль текста
                    style=ft.TextStyle(
                        height=1.2
                    )
                )
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.START,
            # Выравнивание по вертикали
            vertical_alignment=ft.CrossAxisAlignment.START
        )
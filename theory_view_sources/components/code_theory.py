import flet as ft

# Класс для представления виджета с кодом теории
class CodeTheory(ft.Container):
    def __init__(self, code, page):
        super().__init__()
        # Сохраняем ссылки на страницу и код
        self.page = page
        self.code = code
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=32, bottom=32, top=8, right=8)
        self.alignment = ft.alignment.top_left
        self.width = 773
        self.border_radius = 20
        self.bgcolor = ft.colors.ON_SURFACE

        # Создаем столбец с элементами кода
        self.content = ft.Column(
            [
                # Кнопка копирования кода
                ft.IconButton(
                    icon=ft.icons.CONTENT_COPY,
                    on_click=self.copy_code
                ),
                # Текст кода
                ft.Text(
                    self.code,
                    color=ft.colors.BACKGROUND,
                ),
            ],
            spacing=0
        )

    # Метод копирования кода в буфер обмена
    def copy_code(self, e):
        self.page.set_clipboard(self.code)
        self.page.snack_bar = ft.SnackBar(ft.Text("Текст скопирован в буфер обмена!"))
        self.page.snack_bar.open = True
        self.page.update()
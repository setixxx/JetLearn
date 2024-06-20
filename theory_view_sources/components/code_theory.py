import flet as ft

# Класс для представления виджета с кодом теории
class CodeTheory(ft.Container):
    # Инициализация виджета
    def __init__(self, code, page):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Сохранение кода
        self.code = code
        # Установка отступов
        self.padding = ft.padding.only(left=32, bottom=32, top=8, right=8)
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Установка ширины виджета
        self.width = 773
        # Установка радиуса скругления
        self.border_radius = 20
        # Установка фонового цвета
        self.bgcolor = ft.colors.ON_SURFACE
        # Создание столбца с элементами кода
        self.content = ft.Column(
            [
                # Строка с кнопкой копирования
                ft.Row(
                    [
                        # Кнопка копирования
                        ft.IconButton(
                            # Иконка копирования
                            icon=ft.icons.CONTENT_COPY,
                            # Обработчик события клика
                            on_click=self.copy_code
                        ),
                    ],
                    # Выравнивание по горизонтали
                    alignment=ft.MainAxisAlignment.END,
                    # Выравнивание по вертикали
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    # Ширина строки
                    width=773
                ),
                # Строка с текстом кода
                ft.Row(
                    [
                        # Виджет текста кода
                        ft.Text(
                            # Текст кода
                            self.code,
                            # Цвет текста
                            color=ft.colors.BACKGROUND,
                        ),
                    ],
                    # Выравнивание по горизонтали
                    alignment=ft.MainAxisAlignment.START,
                    # Выравнивание по вертикали
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            # Междурядный интервал
            spacing=0
        )

    # Метод копирования кода в буфер обмена
    def copy_code(self, e):
        # Копирование кода в буфер обмена
        self.page.set_clipboard(self.code)
        # Создание сообщения "Текст скопирован в буфер обмена!"
        self.page.snack_bar = ft.SnackBar(ft.Text("Текст скопирован в буфер обмена!"))
        # Отображение сообщения
        self.page.snack_bar.open = True
        # Обновление страницы
        self.page.update()
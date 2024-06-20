import flet as ft


# Класс для представления кнопки изменения темы
class ThemeButton(ft.Column):
    # Инициализация кнопки
    def __init__(self):
        super().__init__()
        # Выравнивание по центру
        self.alignment = ft.MainAxisAlignment.CENTER
        # Выравнивание по горизонтали по центру
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # Междурядный интервал
        self.spacing = 0
        # Создание элементов управления кнопки
        self.controls = [
            # Кнопка с иконкой
            ft.IconButton(
                # Иконка темного режима
                icon=ft.icons.DARK_MODE_OUTLINED,
                # Цвет иконки
                icon_color=ft.colors.ON_SURFACE,
                # Обработчик события клика
                on_click=self.change_theme
            ),
            # Виджет текста для отображения состояния темы
            ft.Text(
                # Текст кнопки
                value="Светлая тема",
                # Вес шрифта
                weight=ft.FontWeight.W_600,
                # Размер текста
                size=16,
                # Выравнивание текста по центру
                text_align=ft.TextAlign.CENTER,
                # Стиль текста
                style=ft.TextStyle(
                    height=1.2
                )
            )
        ]

    # Метод изменения темы
    def change_theme(self, e):
        # Проверка текущей темы
        if self.page.theme_mode == 'dark':
            # Переключение на светлую тему
            self.page.theme_mode = 'light'
            # Изменение иконки на иконку темного режима
            self.controls[0].icon = ft.icons.DARK_MODE_OUTLINED
            # Установка текста кнопки на "Светлая тема"
            self.controls[1].value = "Светлая\nтема"
        else:
            # Переключение на темную тему
            self.page.theme_mode = 'dark'
            # Изменение иконки на иконку светлого режима
            self.controls[0].icon = ft.icons.LIGHT_MODE_OUTLINED
            # Установка текста кнопки на "Темная тема"
            self.controls[1].value = "Темная\nтема"
        # Обновление страницы
        self.page.update()
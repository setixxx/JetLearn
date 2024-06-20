import flet as ft
from main_view_sources.components.profile_image_main import ProfileImageMain

# Класс кнопки "Настройки"
class SettingsButton(ft.Container):
    # Инициализация кнопки
    def __init__(self, page, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Сохранение ссылки на страницу
        self.page = page
        # Установка отступов сверху и справа
        self.padding = ft.padding.only(top=16, right=24)
        # Установка высоты кнопки
        self.height = 113
        # Установка ширины кнопки
        self.width = 1300
        # Создание содержимого кнопки
        self.content = ft.Row(
            [
                # Строка с текстом логина и кнопкой настроек
                ft.Row(
                    [
                        # Виджет текста с логином пользователя
                        ft.Text(
                            # Получение логина из состояния приложения
                            self.app_state.get_login(),
                            # Установка размера текста
                            size=16,
                            # Установка веса шрифта
                            weight=ft.FontWeight.W_500
                        ),
                        # Кнопка настроек с иконкой
                        ft.IconButton(
                            # Иконка пользователя
                            icon=ft.icons.PERSON_OUTLINED,
                            # Цвет иконки
                            icon_color=ft.colors.ON_SURFACE,
                            # Обработчик события клика
                            on_click=lambda e: self.page.go("/main/settings")
                        ),
                        # Виджет с изображением профиля
                        ProfileImageMain()
                    ],
                    # Междуэлементный интервал
                    spacing=8,
                    # Выравнивание по центру
                    alignment=ft.MainAxisAlignment.CENTER,
                    # Вертикальное выравнивание по центру
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            # Междурядный интервал
            spacing=0,
            # Выравнивание по правому краю
            alignment=ft.MainAxisAlignment.END,
            # Вертикальное выравнивание по верхнему краю
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
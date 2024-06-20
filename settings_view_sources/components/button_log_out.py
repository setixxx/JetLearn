import flet as ft

# Класс для представления диалогового окна подтверждения выхода
class ConfirmLogoutDialog(ft.AlertDialog):
    # Инициализация диалогового окна
    def __init__(self):
        super().__init__()
        # Установка режима модального окна
        self.modal = True
        # Создание заголовка "Подтверждение"
        self.title = ft.Text(
            "Подтверждение",
            # Установка веса шрифта
            weight=ft.FontWeight.W_600
        )
        # Создание текста диалогового окна
        self.content = ft.Text("Вы действительно хотите\nвыйти из аккаунта?")
        # Создание списка кнопок
        self.actions = [
            # Кнопка "Да"
            ft.TextButton(
                # Текст кнопки
                text="Да",
                # Обработчик события клика
                on_click=lambda e: self.page.go("/sign_in")
            ),
            # Кнопка "Нет"
            ft.FilledButton(
                # Текст кнопки
                text="Нет",
                # Обработчик события клика
                on_click=self.close_results
            ),
        ]
        # Выравнивание кнопок по правому краю
        self.actions_alignment = ft.MainAxisAlignment.END

    # Метод закрытия диалогового окна
    def close_results(self, e):
        # Установка признака открытости окна в false
        self.open = False
        # Обновление страницы
        self.page.update()

# Класс для представления кнопки "Выйти из аккаунта"
class ButtonLogOut(ft.Row):
    # Инициализация кнопки
    def __init__(self):
        super().__init__()
        # Выравнивание по правому краю
        self.alignment = ft.MainAxisAlignment.END
        # Выравнивание по вертикали по центру
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        # Установка ширины кнопки
        self.width = 1500
        # Установка высоты кнопки
        self.height = 178
        # Создание элемента управления кнопкой
        self.controls = [
            ft.Container(
                # Кнопка "Выйти из аккаунта"
                ft.FilledButton(
                    # Текст кнопки
                    "Выйти из аккаунта",
                    # Обработчик события клика
                    on_click=self.confirm_logout
                ),
                # Отступы справа
                padding=ft.padding.only(right=32)
            )
        ]

    # Метод подтверждения выхода
    def confirm_logout(self, e):
        # Создание диалогового окна подтверждения выхода
        self.page.dialog = ConfirmLogoutDialog()
        # Установка признака открытости окна в true
        self.page.dialog.open = True
        # Обновление страницы
        self.page.update()
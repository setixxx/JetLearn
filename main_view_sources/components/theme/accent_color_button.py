import flet as ft


# Класс для представления элемента всплывающего меню выбора цвета
class PopupColorItem(ft.PopupMenuItem):
    # Инициализация элемента
    def __init__(self, color, name):
        super().__init__()
        # Создание строки с иконкой и названием цвета
        self.content = ft.Row(
            controls=[
                # Иконка цвета
                ft.Icon(name=ft.icons.COLOR_LENS_OUTLINED, color=color),
                # Текст с названием цвета
                ft.Text(name),
            ],
        )
        # Установка обработчика события клика
        self.on_click = self.seed_color_changed
        # Сохранение цвета в качестве данных
        self.data = color

    # Метод обработки изменения цвета
    def seed_color_changed(self, e):
        # Установка цвета в качестве начального цвета темы
        self.page.theme = self.page.dark_theme = ft.theme.Theme(
            color_scheme_seed=self.data
        )
        # Обновление страницы
        self.page.update()


# Класс для представления кнопки выбора цвета
class AccentColorButton(ft.Column):
    # Инициализация кнопки
    def __init__(self):
        super().__init__()
        # Выравнивание по центру
        self.alignment = ft.MainAxisAlignment.CENTER
        # Выравнивание по горизонтали по центру
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # Междурядный интервал
        self.spacing = 0
        # Создание виджета кнопки всплывающего меню
        self.controls = [
            # Кнопка всплывающего меню
            ft.PopupMenuButton(
                # Цвет иконки
                icon_color=ft.colors.ON_SURFACE,
                # Иконка цвета
                icon=ft.icons.COLOR_LENS_OUTLINED,
                # Список элементов меню
                items=[
                    # Элемент меню с темно-фиолетовым цветом
                    PopupColorItem(color="deeppurple",
                                   name="Темно-фиолетовый"),
                    # Элемент меню с индиго цветом
                    PopupColorItem(color="indigo",
                                   name="Индиго"),
                    # Элемент меню с голубым цветом (по умолчанию)
                    PopupColorItem(color="blue",
                                   name="Голубой (по умолчанию)"),
                    # Элемент меню с бирюзовым цветом
                    PopupColorItem(color="teal",
                                   name="Бирюзовый"),
                    # Элемент меню с зеленым цветом
                    PopupColorItem(color="green",
                                   name="Зеленый"),
                    # Элемент меню с желтым цветом
                    PopupColorItem(color="yellow",
                                   name="Желтый"),
                    # Элемент меню с оранжевым цветом
                    PopupColorItem(color="orange",
                                   name="Оранжевый"),
                    # Элемент меню с темно-оранжевым цветом
                    PopupColorItem(color="deeporange",
                                   name="Темно-оранжевый"),
                    # Элемент меню с розовым цветом
                    PopupColorItem(color="pink",
                                   name="Розовый"),
                ]
            ),
            # Виджет текста с подписью "Цвет"
            ft.Text(
                # Текст подписи
                "Цвет",
                # Вес шрифта
                weight=ft.FontWeight.W_600,
                # Размер текста
                size=16
            )
        ]
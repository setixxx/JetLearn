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


# Класс для представления контейнера с кнопками выбора цвета и темы
class AccentColorAndTheme(ft.Container):
    # Инициализация контейнера
    def __init__(self):
        super().__init__()
        # Установка отступов снизу
        self.padding = ft.padding.only(bottom=42)
        # Установка ширины контейнера
        self.width = 100
        # Установка высоты контейнера
        self.height = 370
        # Создание столбца с кнопками
        self.content = ft.Column(
            [
                # Кнопка выбора цвета
                AccentColorButton(),
                # Кнопка выбора темы
                ThemeButton(),
            ],
            # Выравнивание по правому краю
            alignment=ft.MainAxisAlignment.END,
            # Выравнивание по горизонтали по центру
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
# Импортируем библиотеку flet
import flet as ft

# Импортируем компоненты из подкаталогов
from accent_color_and_theme import \
    AccentColorAndTheme

# Класс для представления боковой панели навигации
class NavigationRail(ft.Container):
    def __init__(self, change_view_callback):
        super().__init__()
        # Устанавливаем стили контейнера
        self.alignment = ft.alignment.top_left
        self.width = 200
        self.height = 370
        # Создаем виджет боковой панели навигации
        self.content = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            height=364,
            width=100,
            group_alignment=-1.0,
            destinations=[
                # Пункт навигации "Теория"
                ft.NavigationRailDestination(
                    icon=ft.icons.BOOK_OUTLINED,
                    selected_icon=ft.icons.BOOK,
                    label_content=ft.Text(
                        "Теория",
                        size=16,
                        weight=ft.FontWeight.W_600
                    ),
                ),
                # Пункт навигации "Тесты"
                ft.NavigationRailDestination(
                    icon=ft.icons.BROWSE_GALLERY_OUTLINED,
                    selected_icon=ft.icons.BROWSE_GALLERY,
                    label_content=ft.Text(
                        "Тесты",
                        size=16,
                        weight=ft.FontWeight.W_600
                    )
                ),
                # Пункт навигации "Тренажер"
                ft.NavigationRailDestination(
                    icon=ft.icons.VIEW_IN_AR_OUTLINED,
                    selected_icon=ft.icons.VIEW_IN_AR,
                    label_content=ft.Text(
                        "Тренажер",
                        size=16,
                        weight=ft.FontWeight.W_600
                    )
                )
            ],
            on_change=change_view_callback
        )

# Класс для представления отдельной карточки практики
class PracticeCard(ft.Container):
    def __init__(self, text, image, destination):
        super().__init__()
        # Сохраняем ссылки на текст, изображение и маршрут перехода
        self.destination = destination
        self.text = text
        self.image = image
        # Устанавливаем обработчики событий наведения и клика
        self.on_hover = self.on_hover_handler
        self.on_click = destination
        # Устанавливаем стили контейнера
        self.bgcolor = ft.colors.SECONDARY_CONTAINER
        self.border_radius = 12
        self.width = 435
        self.height = 625
        # Создаем столбец с содержимым карточки
        self.content = ft.Column(
            [
                # Изображение
                ft.Image(
                    src=image,
                    width=435,
                    height=406,
                    border_radius=12,
                    fit=ft.ImageFit.COVER
                ),
                # Текст карточки
                ft.Container(
                    ft.Text(
                        value=text,
                        size=48,
                        weight=ft.FontWeight.W_600,
                        text_align=ft.TextAlign.START,
                        style=ft.TextStyle(
                            height=1
                        ),
                    ),
                    width=435,
                    height=220,
                    alignment=ft.alignment.top_left,
                    padding=16
                )
            ],
            spacing=0
        )

    # Обработчик события наведения мыши
    def on_hover_handler(self, e):
        # Изменяем фоновый цвет карточки при наведении
        self.bgcolor = ft.colors.GREY_400 if e.data == "true" else ft.colors.SECONDARY_CONTAINER
        self.update()

# Класс для представления контейнера с карточкой практики
class PracticeCards(ft.Container):
    def __init__(self, page):
        super().__init__()
        # Сохраняем ссылку на страницу
        self.page = page
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(bottom=42)
        self.alignment = ft.alignment.center
        self.width = 1300
        self.height = 688
        # Создаем столбец с карточкой практики
        self.content = ft.Column(
            [
                # Карточка практики
                PracticeCard("Тренажер по\nвсему курсу",
                             f"assets/practice.png",
                             lambda e: self.page.go("/main/practice")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

# Класс для представления изображения профиля
class ProfileImageMain(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.bgcolor = ft.colors.PRIMARY
        self.width = 40
        self.height = 40
        self.border_radius = 40

# Класс кнопки "Настройки"
class SettingsButton(ft.Container):
    def __init__(self, page, app_state):
        super().__init__()
        # Сохраняем ссылки на страницу и состояние приложения
        self.app_state = app_state
        self.page = page
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(top=16, right=24)
        self.height = 113
        self.width = 1300
        # Создаем содержимое кнопки
        self.content = ft.Row(
            [
                # Строка с текстом логина и кнопкой настроек
                ft.Row(
                    [
                        # Текст с логином пользователя
                        ft.Text(
                            self.app_state.get_login(),
                            size=16,
                            weight=ft.FontWeight.W_500
                        ),
                        # Кнопка настроек с иконкой
                        ft.IconButton(
                            icon=ft.icons.PERSON_OUTLINED,
                            icon_color=ft.colors.ON_SURFACE,
                            on_click=lambda e: self.page.go("/main/settings")
                        ),
                        # Изображение профиля
                        ProfileImageMain()
                    ],
                    spacing=8,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

# Класс для представления отдельной карточки теста
class TestCard(ft.Container):
    def __init__(self, text, image, destination):
        super().__init__()
        # Сохраняем ссылки на текст, изображение и маршрут перехода
        self.destination = destination
        self.text = text
        self.image = image
        # Устанавливаем обработчики событий наведения и клика
        self.on_hover = self.on_hover_handler
        self.on_click = destination
        # Устанавливаем стили контейнера
        self.bgcolor = ft.colors.SECONDARY_CONTAINER
        self.border_radius = 12
        self.width = 231
        self.height = 303
        # Создаем столбец с содержимым карточки
        self.content = ft.Column(
            [
                # Изображение
                ft.Image(
                    src=image,
                    width=231,
                    height=197,
                    border_radius=12,
                    fit=ft.ImageFit.COVER
                ),
                # Текст карточки
                ft.Container(
                    ft.Text(
                        value=text,
                        size=24,
                        weight=ft.FontWeight.W_600,
                        text_align=ft.TextAlign.START,
                        style=ft.TextStyle(
                            height=1
                        ),
                    ),
                    width=231,
                    height=106,
                    alignment=ft.alignment.top_left,
                    padding=16
                )
            ],
            spacing=0
        )

    # Обработчик события наведения мыши
    def on_hover_handler(self, e):
        # Изменяем фоновый цвет карточки при наведении
        self.bgcolor = ft.colors.GREY_400 if e.data == "true" else ft.colors.SECONDARY_CONTAINER
        self.update()

# Класс для представления сетки карточек тестов
class TestCards(ft.Container):
    def __init__(self, page):
        super().__init__()
        # Сохраняем ссылку на страницу
        self.page = page
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=77)
        self.alignment = ft.alignment.top_left
        self.width = 1300
        self.height = 688
        # Создаем столбец с карточками
        self.content = ft.Column(
            [
                # Строка с карточками
                ft.Row(
                    [
                        # Первая карточка
                        TestCard("Тест \nпо первому модулю",
                                   "assets/jetpack_compose.png",
                                   lambda e: self.page.go("/main/test_1")),
                        # Вторая карточка
                        TestCard("Тест \nпо второму\nмодулю",
                                   "assets/components.png",
                                   lambda e: self.page.go("/main/test_2")),
                        # Третья карточка
                        TestCard("Тест \nпо третьему модулю",
                                   "assets/modifier.png",
                                   lambda e: self.page.go("/main/test_4")),
                        # Четвертая карточка
                        TestCard("Тест \nпо четвертому модулю",
                                   "assets/rows.png",
                                   lambda e: self.page.go("/main/test_5")),
                    ],
                    spacing=40
                ),
                # Строка с карточками
                ft.Row(
                    [
                        # Пятая карточка
                        TestCard("Тест \nпо пятому\nмодулю",
                                   "assets/lazy_components.png",
                                   lambda e: self.page.go("/main/test_6")),
                        # Шестая карточка
                        TestCard("Тест \nпо шестому\nмодулю",
                                   "assets/state.png",
                                   lambda e: self.page.go("/main/test_3")),
                        # Седьмая карточка
                        TestCard("Тест \nпо седьмому модулю",
                                   "assets/images_image.png",
                                   lambda e: self.page.go("/main/test_7")),
                        # Восьмая карточка
                        TestCard("Тест \nпо восьмому модулю",
                                   "assets/material_design.png",
                                   lambda e: self.page.go("/main/test_8")),
                    ],
                    spacing=40
                )
            ],
            spacing=40
        )

# Класс для представления отдельной карточки теории
class TheoryCard(ft.Container):
    def __init__(self, text, image, destination):
        super().__init__()
        # Сохраняем ссылки на текст, изображение и маршрут перехода
        self.destination = destination
        self.text = text
        self.image = image
        # Устанавливаем обработчики событий наведения и клика
        self.on_hover = self.on_hover_handler
        self.on_click = destination
        # Устанавливаем стили контейнера
        self.bgcolor = ft.colors.SECONDARY_CONTAINER
        self.border_radius = 12
        self.width = 231
        self.height = 303
        # Создаем столбец с содержимым карточки
        self.content = ft.Column(
            [
                # Изображение
                ft.Image(
                    src=image,
                    width=231,
                    height=197,
                    border_radius=12,
                    fit=ft.ImageFit.COVER
                ),
                # Текст карточки
                ft.Container(
                    ft.Text(
                        value=text,
                        size=24,
                        weight=ft.FontWeight.W_600,
                        text_align=ft.TextAlign.START,
                        style=ft.TextStyle(
                            height=1
                        ),
                    ),
                    width=231,
                    height=106,
                    alignment=ft.alignment.top_left,
                    padding=16
                )
            ],
            spacing=0
        )

    # Обработчик события наведения мыши
    def on_hover_handler(self, e):
        # Изменяем фоновый цвет карточки при наведении
        self.bgcolor = ft.colors.GREY_400 if e.data == "true" else ft.colors.SECONDARY_CONTAINER
        self.update()

# Класс для представления сетки карточек теории
class TheoryCards(ft.Container):
    def __init__(self, page):
        super().__init__()
        # Сохраняем ссылку на страницу
        self.page = page
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=77)
        self.alignment = ft.alignment.top_left
        self.width = 1300
        self.height = 688
        # Создаем столбец с карточками
        self.content = ft.Column(
            [
                # Строка с карточками
                ft.Row(
                    [
                        # Первая карточка
                        TheoryCard("Введение \nв Jetpack\nCompose",
                                   "assets/jetpack_compose.png",
                                   lambda e: self.page.go("/main/theory_1")),
                        # Вторая карточка
                        TheoryCard("Компоненты Compose и @Composable",
                                   "assets/components.png",
                                   lambda e: self.page.go("/main/theory_2")),
                        # Третья карточка
                        TheoryCard("Модификаторы и стили",
                                   "assets/modifier.png",
                                   lambda e: self.page.go("/main/theory_4")),
                        # Четвертая карточка
                        TheoryCard("Макеты и расположение",
                                   "assets/rows.png",
                                   lambda e: self.page.go("/main/theory_5")),
                    ],
                    spacing=40
                ),
                # Строка с карточками
                ft.Row(
                    [
                        # Пятая карточка
                        TheoryCard("Списки и отображение данных",
                                   "assets/lazy_components.png",
                                   lambda e: self.page.go("/main/theory_6")),
                        # Шестая карточка
                        TheoryCard("Состояние и перерисовка",
                                   "assets/state.png",
                                   lambda e: self.page.go("/main/theory_3")),
                        # Седьмая карточка
                        TheoryCard("Изображения \nи ресурсы \nв Compose",
                                   "assets/images_image.png",
                                   lambda e: self.page.go("/main/theory_7")),
                        # Восьмая карточка
                        TheoryCard("Тема оформления и Material Design",
                                   "assets/material_design.png",
                                   lambda e: self.page.go("/main/theory_8")),
                    ],
                    spacing=40
                )
            ],
            spacing=40
        )

# Класс для представления логотипа
class Logo(ft.Container):
    # Инициализация логотипа
    def __init__(self):
        super().__init__()
        # Установка ширины логотипа
        self.width = 200
        # Установка высоты логотипа
        self.height = 60
        # Выравнивание по левому краю
        self.alignment = ft.alignment.center_left
        # Установка отступов слева
        self.padding = ft.padding.only(left=24)
        # Создание виджета текста для логотипа
        self.content = ft.Text(
            # Текст логотипа
            "JetLearn",
            # Размер текста
            size=32,
            # Вес шрифта
            weight=ft.FontWeight.W_500
        )

# Класс основного представления
class MainView(ft.View):
    # Инициализация основного представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        self.app_state = app_state
        self.page = page
        self.padding = 0
        self.route = "/main"
        # Инициализация компонентов
        self.navigation_rail = NavigationRail(self.change_view)
        self.theory_cards = TheoryCards(self.page)
        self.test_cards = TestCards(self.page)
        self.practice_card = PracticeCards(self.page)
        self.current_view = "Теория"
        # Обновление представления
        self.update_view()

    # Метод обновления представления
    def update_view(self):
        # Выбор карточек в зависимости от текущего представления
        match self.current_view:
            case "Теория":
                cards = self.theory_cards
            case "Тесты":
                cards = self.test_cards
            case "Практика":
                cards = self.practice_card
            case _:
                cards = ft.Container()

        # Очистка и добавление элементов в представление
        self.controls.clear()
        self.controls.append(
            ft.Container(
                ft.Row(
                    [
                        ft.Column(
                            [
                                Logo(),
                                self.navigation_rail,
                                AccentColorAndTheme()
                            ],
                            spacing=0
                        ),
                        ft.Column(
                            [
                                SettingsButton(self.page, self.app_state),
                                cards
                            ],
                            spacing=0
                        )
                    ],
                    spacing=0
                ),
                width=1500,
                height=800,
            )
        )
        # Обновление страницы
        self.page.update()

    # Метод обработки изменения представления
    def change_view(self, e):
        # Получение индекса выбранного элемента
        selected_index = e.control.selected_index
        # Обновление текущего представления в зависимости от индекса
        if selected_index == 0:
            self.current_view = "Теория"
        elif selected_index == 1:
            self.current_view = "Тесты"
        elif selected_index == 2:
            self.current_view = "Практика"

        # Обновление представления
        self.update_view()
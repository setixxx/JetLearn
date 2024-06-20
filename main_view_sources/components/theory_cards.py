import flet as ft

# Класс для представления отдельной карточки теории
class TheoryCard(ft.Container):
    # Инициализация карточки с текстом, изображением и маршрутом перехода
    def __init__(self, text, image, destination):
        super().__init__()
        # Сохранение маршрута перехода
        self.destination = destination
        # Сохранение текста карточки
        self.text = text
        # Сохранение пути к изображению
        self.image = image
        # Установка обработчика события наведения мыши
        self.on_hover = self.on_hover_handler
        # Установка обработчика события клика
        self.on_click = destination
        # Установка фонового цвета карточки
        self.bgcolor = ft.colors.SECONDARY_CONTAINER
        # Установка радиуса скругления карточки
        self.border_radius = 12
        # Установка ширины карточки
        self.width = 231
        # Установка высоты карточки
        self.height = 303
        # Создание столбца с содержимым карточки
        self.content = ft.Column(
            [
                # Виджет изображения
                ft.Image(
                    # Путь к изображению
                    src=image,
                    # Ширина изображения
                    width=231,
                    # Высота изображения
                    height=197,
                    # Радиус скругления изображения
                    border_radius=12,
                    # Способ отображения изображения
                    fit=ft.ImageFit.COVER
                ),
                # Виджет контейнера для текста
                ft.Container(
                    # Виджет текста
                    ft.Text(
                        # Текст карточки
                        value=text,
                        # Размер текста
                        size=24,
                        # Вес шрифта
                        weight=ft.FontWeight.W_600,
                        # Выравнивание текста
                        text_align=ft.TextAlign.START,
                        # Стиль текста
                        style=ft.TextStyle(
                            height=1
                        ),
                    ),
                    # Ширина контейнера
                    width=231,
                    # Высота контейнера
                    height=106,
                    # Выравнивание содержимого
                    alignment=ft.alignment.top_left,
                    # Отступы
                    padding=16
                )
            ],
            # Междурядный интервал
            spacing=0
        )

    # Обработчик события наведения мыши
    def on_hover_handler(self, e):
        # Изменение фонового цвета карточки при наведении
        self.bgcolor = ft.colors.GREY_400 if e.data == "true" \
            else ft.colors.SECONDARY_CONTAINER
        # Обновление карточки
        self.update()


# Класс для представления сетки карточек теории
class TheoryCards(ft.Container):
    # Инициализация сетки карточек
    def __init__(self, page):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Установка отступов слева
        self.padding = ft.padding.only(left=77)
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Установка ширины сетки
        self.width = 1300
        # Установка высоты сетки
        self.height = 688
        # Создание столбца с карточками
        self.content = ft.Column(
            [
                # Строка с карточками
                ft.Row(
                    [
                        # Создание первой карточки
                        TheoryCard("Введение \nв Jetpack\nCompose",
                                   "assets/jetpack_compose.png",
                                   lambda e: self.page.go("/main/theory_1")),
                        # Создание второй карточки
                        TheoryCard("Компоненты Compose и @Composable",
                                   "assets/components.png",
                                   lambda e: self.page.go("/main/theory_2")),
                        # Создание третьей карточки
                        TheoryCard("Модификаторы и стили",
                                   "assets/modifier.png",
                                   lambda e: self.page.go("/main/theory_4")),
                        # Создание четвертой карточки
                        TheoryCard("Макеты и расположение",
                                   "assets/rows.png",
                                   lambda e: self.page.go("/main/theory_5")),
                    ],
                    # Междуэлементный интервал
                    spacing=40
                ),
                # Строка с карточками
                ft.Row(
                    [
                        # Создание пятой карточки
                        TheoryCard("Списки и отображение данных",
                                   "assets/lazy_components.png",
                                   lambda e: self.page.go("/main/theory_6")),
                        # Создание шестой карточки
                        TheoryCard("Состояние и перерисовка",
                                   "assets/state.png",
                                   lambda e: self.page.go("/main/theory_3")),
                        # Создание седьмой карточки
                        TheoryCard("Изображения \nи ресурсы \nв Compose",
                                   "assets/images_image.png",
                                   lambda e: self.page.go("/main/theory_7")),
                        # Создание восьмой карточки
                        TheoryCard("Тема оформления и Material Design",
                                   "assets/material_design.png",
                                   lambda e: self.page.go("/main/theory_8")),
                    ],
                    # Междуэлементный интервал
                    spacing=40
                )
            ],
            # Междурядный интервал
            spacing=40
        )
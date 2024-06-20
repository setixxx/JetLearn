import flet as ft

# Класс для представления отдельной карточки практики
class PracticeCard(ft.Container):
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
        self.width = 435
        # Установка высоты карточки
        self.height = 625
        # Создание столбца с содержимым карточки
        self.content = ft.Column(
            [
                # Виджет изображения
                ft.Image(
                    # Путь к изображению
                    src=image,
                    # Ширина изображения
                    width=435,
                    # Высота изображения
                    height=406,
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
                        size=48,
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
                    width=435,
                    # Высота контейнера
                    height=220,
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


# Класс для представления контейнера с карточкой практики
class PracticeCards(ft.Container):
    # Инициализация контейнера
    def __init__(self, page):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Установка отступов снизу
        self.padding = ft.padding.only(bottom=42)
        # Выравнивание по центру
        self.alignment = ft.alignment.center
        # Установка ширины контейнера
        self.width = 1300
        # Установка высоты контейнера
        self.height = 688
        # Создание столбца с карточкой практики
        self.content = ft.Column(
            [
                # Создание карточки практики
                PracticeCard("Тренажер по\nвсему курсу",
                             f"assets/practice.png",
                             lambda e: self.page.go("/main/practice")),
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.CENTER,
            # Выравнивание по вертикали
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
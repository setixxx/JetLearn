import flet as ft

class GitHubLinkAndImage(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.center_right
        self.width = 200
        self.height = 75
        self.content = ft.ListTile(
            title=ft.Text(
                value="Cоздал setixx",
                size=16,
                weight=ft.FontWeight.W_400,
                max_lines=1,
                text_align=ft.TextAlign.END
            ),
            trailing=ft.Image(
                src=f"assets/github.png",
                height=24,
                width=24,
                fit=ft.ImageFit.COVER,
            ),
            url="https://github.com/setixxx",
            shape=ft.RoundedRectangleBorder(radius=10),
        )

# Класс для представления виджета кнопки "Начать обучение"
class ButtonStart(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(top=21)
        self.width = 1198
        self.height = 212
        self.content = ft.Row(
            [
                # Кнопка "Начать обучение"
                ft.FilledButton(
                    text="Начать обучение",
                    icon="TOKEN_OUTLINED",
                    width=238,
                    height=63,
                    on_click=lambda e: self.page.go("/sign_in")
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START
        )

class IntroductionText(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 1200
        self.height = 85
        self.content = ft.Row(
            [
                ft.Text(
                    value="Начните своё путешествие в мир Jetpack Compose – "
                          "создавайте удивительные\nинтерфейсы"
                          "уже сегодня!",
                    size=16,
                    weight=ft.FontWeight.W_700,
                    text_align=ft.TextAlign.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

class WelcomeText(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 1200
        self.height = 228
        self.content = ft.Row(
            [
                ft.Text(
                    value="Добро пожаловать \nв JetLearn",
                    size=56,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextStyle(
                        height=1.2,
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

# Класс представления начальной страницы
class StartView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        # Сохраняем ссылку на страницу
        self.page = page
        # Устанавливаем маршрут
        self.route = "/"
        # Устанавливаем отступы
        self.padding = 0

        # Создаем элементы представления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Контейнер для приветствия, введения и кнопки "Начать"
                        ft.Container(
                            ft.Column(
                                [
                                    WelcomeText(),
                                    IntroductionText(),
                                    ButtonStart(),
                                ],
                                spacing=0
                            ),
                            margin=0,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=40
                        ),
                        # Строка с ссылкой на GitHub
                        ft.Row(
                            [
                                GitHubLinkAndImage()
                            ],
                            width=1200,
                            height=75,
                            alignment=ft.MainAxisAlignment.END,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                    ],
                    spacing=0,
                ),
                margin=ft.padding.only(top=100, left=150, right=150, bottom=175),
                width=1200,
                height=600,
            )
        ]
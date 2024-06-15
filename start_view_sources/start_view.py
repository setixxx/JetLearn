import flet as ft
from start_view_sources.components.welcome_text import WelcomeText
from start_view_sources.components.introduction_text import IntroductionText
from start_view_sources.components.button_start import ButtonStart
from start_view_sources.components.github_link_and_image import \
    GitHubLinkAndImage


class StartView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = "/"
        self.padding = 0

        self.welcome_text = WelcomeText()
        self.introduction_text = IntroductionText()
        self.button_start = ButtonStart()
        self.github_link_and_image = GitHubLinkAndImage()

        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Column(
                                [
                                    self.welcome_text,
                                    self.introduction_text,
                                    self.button_start,
                                ],
                                spacing=0
                            ),
                            margin=0,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=40
                        ),
                        ft.Row(
                            [
                                self.github_link_and_image
                            ],
                            width=1200,
                            height=75,
                            alignment=ft.MainAxisAlignment.END,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                    ],
                    spacing=0,
                ),
                margin=ft.padding.only(top=100,
                                       left=150,
                                       right=150,
                                       bottom=175),
                width=1200,
                height=600,
            )
        ]

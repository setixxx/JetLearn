import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from theory_view_sources.components.first_theory_text import FirstTheoryText

# Класс представления первого раздела теории
class FirstTheoryView(ft.View):
    # Инициализация представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Установка маршрута
        self.route = "/main/theory_1"
        # Установка отступов
        self.padding = 0
        # Создание списка элементов управления
        self.controls = [
            ft.Container(
                ft.Row(
                    [
                        # Столбец для кнопки "Назад" и логотипа
                        ft.Column(
                            [
                                # Кнопка "Назад" и логотип
                                ArrowBackAndLogo(
                                    lambda e: self.page.go("/main")
                                )
                            ]
                        ),
                        # Контейнер для текста первого раздела теории
                        ft.Container(
                            ft.Column(
                                [
                                    # Виджет текста первого раздела теории
                                    FirstTheoryText(page, app_state)
                                ],
                                # Включение автоматической прокрутки
                                scroll=ft.ScrollMode.AUTO
                            ),
                            # Отступы сверху
                            margin=ft.padding.only(top=76)
                        ),
                    ]
                ),
                # Ширина контейнера
                width=1500,
                # Высота контейнера
                height=800,
            )
        ]
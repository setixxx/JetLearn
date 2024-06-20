import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from theory_view_sources.components.code_theory import CodeTheory
import json
from database import DatabaseManager

json_file_path = 'data/theory.json'


# Функция для загрузки данных из JSON файла
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data


# Класс для представления текста первого раздела теории
class FirstTheoryText(ft.Container):
    def __init__(self, page, app_state):
        super().__init__()
        # Сохраняем ссылки на страницу, объект базы данных и состояние
        # приложения
        self.page = page
        self.database = DatabaseManager("users.sqlite")
        self.app_state = app_state
        # Устанавливаем стили контейнера
        self.margin = ft.padding.only(right=39, bottom=32)
        self.alignment = ft.alignment.bottom_left
        self.width = 812
        self.height = 2000

        # Создаем кнопку "Назад"
        self.button_go_back = ft.TextButton("Назад")
        self.button_go_back.disabled = True

        # Загружаем данные из JSON файла
        json_data = load_json_data(json_file_path)

        # Создаем карточку с текстом первого раздела теории
        self.content = ft.Card(
            ft.Container(
                ft.Column(
                    [
                        # Заголовок раздела
                        ft.Text(json_data[0]["title"], size=28,
                                weight=ft.FontWeight.W_600),
                        # Текст первого раздела теории
                        ft.Text(json_data[0]["content"][0], size=20),
                        ft.Text(json_data[0]["content"][1], size=20),
                        ft.Text(json_data[0]["content"][2], size=20),
                        # Виджет с примером кода
                        CodeTheory(json_data[0]["code_examples"][0], page),
                        ft.Text(json_data[0]["content"][3], size=20),
                        ft.Text(json_data[0]["content"][4], size=20),
                        ft.Text(json_data[0]["content"][5], size=20),
                        ft.Text(json_data[0]["content"][6], size=20),
                        # Контейнер для кнопок "Назад" и "Вперед"
                        ft.Container(
                            ft.Row(
                                [
                                    self.button_go_back,
                                    # Кнопка "Вперед"
                                    ft.FilledButton(
                                        "Вперед",
                                        on_click=lambda
                                            e: self.update_theory_state(
                                            self.app_state.get_login(),
                                            "THEORY_1"
                                        )
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                vertical_alignment=ft.CrossAxisAlignment.END
                            ),
                            padding=ft.padding.only(top=26),
                            width=773
                        )
                    ]
                ),
                padding=ft.padding.only(top=48, left=48, right=48),
            ),
            width=773
        )

    # Метод обновления состояния теории в базе данных
    def update_theory_state(self, login, theory):
        # Обновляем состояние теории в базе данных
        self.database.update_theory(login, theory, True)
        # Получаем количество пройденных разделов теории
        completed_theory = self.database.get_completed_theory_count(login)
        # Устанавливаем количество пройденных разделов теории в состоянии приложения
        self.app_state.set_completed_theory(completed_theory)
        # Переходим к следующему разделу теории
        self.page.go("/main/theory_2")


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
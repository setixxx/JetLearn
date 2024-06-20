import flet as ft
from theory_view_sources.components.code_theory import \
    CodeTheory
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
    # Инициализация виджета текста первого раздела теории
    def __init__(self, page, app_state):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Создание объекта базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохранение состояния приложения
        self.app_state = app_state
        # Установка отступов справа и снизу
        self.margin = ft.padding.only(right=39, bottom=32)
        # Выравнивание по левому нижнему краю
        self.alignment = ft.alignment.bottom_left
        # Установка ширины виджета
        self.width = 812
        # Установка высоты виджета
        self.height = 2000
        # Создание кнопки "Назад"
        self.button_go_back = ft.TextButton(
            "Назад",
        )
        # Деактивация кнопки "Назад"
        self.button_go_back.disabled = True

        # Загрузка данных из JSON файла
        json_data = load_json_data(json_file_path)

        # Создание карточки с текстом первого раздела теории
        self.content = ft.Card(
            ft.Container(
                # Создание столбца с текстом
                ft.Column(
                    [
                        # Заголовок раздела
                        ft.Text(
                            # Текст заголовка
                            json_data[0]["title"],
                            # Размер текста
                            size=28,
                            # Вес шрифта
                            weight=ft.FontWeight.W_600
                        ),
                        # Текст первого раздела
                        ft.Text(
                            # Текст первого раздела
                            json_data[0]["content"][0],
                            # Размер текста
                            size=20
                        ),
                        # Текст второго раздела
                        ft.Text(
                            # Текст второго раздела
                            json_data[0]["content"][1],
                            # Размер текста
                            size=20
                        ),
                        # Текст третьего раздела
                        ft.Text(
                            # Текст третьего раздела
                            json_data[0]["content"][2],
                            # Размер текста
                            size=20
                        ),
                        # Виджет с примером кода
                        CodeTheory(json_data[0]["code_examples"][0], page),
                        # Текст четвертого раздела
                        ft.Text(
                            # Текст четвертого раздела
                            json_data[0]["content"][3],
                            # Размер текста
                            size=20
                        ),
                        # Текст пятого раздела
                        ft.Text(
                            # Текст пятого раздела
                            json_data[0]["content"][4],
                            # Размер текста
                            size=20
                        ),
                        # Текст шестого раздела
                        ft.Text(
                            # Текст шестого раздела
                            json_data[0]["content"][5],
                            # Размер текста
                            size=20
                        ),
                        # Текст седьмого раздела
                        ft.Text(
                            # Текст седьмого раздела
                            json_data[0]["content"][6],
                            # Размер текста
                            size=20
                        ),
                        # Контейнер для кнопок "Назад" и "Вперед"
                        ft.Container(
                            # Создание строки с кнопками
                            ft.Row(
                                [
                                    # Кнопка "Назад"
                                    self.button_go_back,
                                    # Кнопка "Вперед"
                                    ft.FilledButton(
                                        # Текст кнопки
                                        "Вперед",
                                        # Обработчик события клика
                                        on_click=lambda e:
                                        self.update_theory_state(
                                            self.app_state.get_login(),
                                            "THEORY_1"
                                        )
                                    )
                                ],
                                # Выравнивание по горизонтали
                                alignment=ft.MainAxisAlignment.END,
                                # Выравнивание по вертикали
                                vertical_alignment=ft.CrossAxisAlignment.END
                            ),
                            # Отступы сверху
                            padding=ft.padding.only(top=26),
                            # Ширина контейнера
                            width=773
                        )
                    ]
                ),
                # Отступы вокруг контейнера
                padding=ft.padding.only(top=48, left=48, right=48),
            ),
            # Ширина карточки
            width=773
        )

    # Метод обновления состояния теории в базе данных
    def update_theory_state(self, login, theory):
        # Обновление состояния теории в базе данных
        self.database.update_theory(login, theory, True),
        # Получение количества пройденных разделов теории
        completed_theory = self.database.get_completed_theory_count(login)
        # Установка количества пройденных разделов теории в состоянии приложения
        self.app_state.set_completed_theory(completed_theory),
        # Переход к следующему разделу теории
        self.page.go("/main/theory_2")
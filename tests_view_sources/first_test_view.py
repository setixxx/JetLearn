import flet as ft
import json
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from tests_view_sources.components.first_test import FirstTest

# Класс FirstTestView представляет вид первого теста
class FirstTestView(ft.View):
    def __init__(self, page: ft.Page, db_manager, app_state):
        super().__init__()
        self.page = page
        # Менеджер базы данных для выполнения операций с БД
        self.db_manager = db_manager
        # Объект состояния приложения для хранения текущего состояния
        self.app_state = app_state
        self.padding = 0
        # Маршрут для первого теста
        self.route = "/main/test_1"
        # Загрузка вопросов при инициализации
        self.load_questions()

    # Метод load_questions загружает вопросы из JSON-файла и
    # создает интерфейс теста
    def load_questions(self):
        # Открытие файла с вопросами и загрузка данных
        with open("data/test.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            questions = data[0]["questions"]

        # Определение элементов интерфейса
        self.controls = [
            ft.Container(
                ft.Row(
                    [
                        # Левая колонка с кнопкой "Назад" и логотипом
                        ft.Column(
                            [
                                ArrowBackAndLogo(
                                    # Переход на главный экран при нажатии
                                    lambda e: self.page.go("/main")
                                )
                            ]
                        ),
                        # Правая колонка с тестом
                        ft.Container(
                            ft.Column(
                                [
                                    FirstTest(self.page,
                                              questions,
                                              self.restart_test,
                                              self.db_manager,
                                              self.app_state)
                                ],
                                scroll=ft.ScrollMode.AUTO
                            ),
                            margin=ft.padding.only(top=76)
                        )
                    ]
                ),
                width=1500,
                height=800,
            )
        ]

    # Метод restart_test перезагружает вопросы и обновляет страницу
    def restart_test(self):
        self.load_questions()  # Повторная загрузка вопросов
        self.page.update()  # Обновление страницы для отображения новых данных

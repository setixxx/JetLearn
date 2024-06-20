import flet as ft

# Класс ResultsDialog представляет диалоговое окно с результатами теста
class ResultsDialog(ft.AlertDialog):
    def __init__(self, correct_answers, total_questions, restart_test, db_manager, app_state, test_number):
        super().__init__()
        self.test_number = test_number  # Номер теста для обновления в базе данных
        self.modal = True  # Диалог является модальным
        self.correct_answers = correct_answers  # Количество правильных ответов
        self.total_questions = total_questions  # Общее количество вопросов
        self.restart_test = restart_test  # Функция для перезапуска теста
        self.db_manager = db_manager  # Менеджер базы данных для выполнения операций с БД
        self.app_state = app_state  # Объект состояния приложения для хранения текущего состояния
        self.title = ft.Text(
            "Результаты теста",
            weight=ft.FontWeight.W_600  # Полужирный текст
        )
        self.content = TextResults(correct_answers, total_questions)  # Контент с результатами теста
        self.actions = [
            ft.TextButton(
                text="Закончить",
                on_click=self.close_results  # Закрытие диалога и сохранение результатов
            ),
            ft.FilledButton(
                "Начать заново",
                on_click=self.start_again  # Перезапуск теста
            ),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END  # Выравнивание кнопок

    # Метод close_results закрывает диалог и сохраняет результаты
    def close_results(self, e):
        self.record_results()  # Сохранение результатов в базе данных
        self.open = False  # Закрытие диалога
        self.page.update()  # Обновление страницы
        self.page.go("/main")  # Переход на главный экран

    # Метод start_again перезапускает тест
    def start_again(self, e):
        self.close_results(e)  # Закрытие диалога и сохранение результатов
        self.restart_test()  # Перезапуск теста

    # Метод record_results сохраняет результаты теста в базе данных
    def record_results(self):
        login = self.app_state.get_login()  # Получение логина пользователя
        self.db_manager.update_tests(login, self.test_number, self.correct_answers)  # Обновление результатов теста в базе данных
        completed_tests = self.db_manager.get_completed_tests_count(login)  # Получение количества завершенных тестов
        self.app_state.set_completed_tests(completed_tests)  # Обновление состояния приложения


# Класс TextResults представляет контейнер с текстовыми результатами теста
class TextResults(ft.Container):
    def __init__(self, correct_answers, total_questions):
        super().__init__()
        self.height = 70  # Высота контейнера
        self.content = ft.Column(
            [
                ft.Text(
                    f"Отвечено правильно: {correct_answers}/{total_questions}",  # Текст с количеством правильных ответов
                    size=16
                ),
                ft.Text(
                    f"Ваша оценка: {correct_answers * 5 // total_questions}",  # Текст с оценкой
                    size=16
                )
            ]
        )


# Класс Results представляет контейнер с кнопкой для завершения теста и отображения результатов
class Results(ft.Container):
    def __init__(self, page, test_texts, restart_test, db_manager, app_state, test_number):
        super().__init__()
        self.test_number = test_number  # Номер теста для обновления в базе данных
        self.page = page  # Страница, на которой отображается тест
        self.test_texts = test_texts  # Список объектов TestText
        self.restart_test = restart_test  # Функция для перезапуска теста
        self.db_manager = db_manager  # Менеджер базы данных для выполнения операций с БД
        self.app_state = app_state  # Объект состояния приложения для хранения текущего состояния
        self.padding = ft.padding.only(top=16, bottom=16)  # Отступы контейнера
        self.border_radius = 20  # Радиус границ контейнера
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.FilledButton(
                            "Закончить",
                            on_click=self.open_test_results  # Открытие диалога с результатами теста
                        )
                    ],
                    spacing=16
                )
            ],
            alignment=ft.MainAxisAlignment.END  # Выравнивание кнопки
        )

    # Метод open_test_results открывает диалог с результатами теста
    def open_test_results(self, e):
        correct_answers = sum([test_text.check_answer() for test_text in self.test_texts])  # Подсчет правильных ответов
        total_questions = len(self.test_texts)  # Общее количество вопросов
        self.page.dialog = ResultsDialog(correct_answers,
                                         total_questions,
                                         self.restart_test,
                                         self.db_manager,
                                         self.app_state,
                                         self.test_number)  # Создание диалога с результатами
        self.page.dialog.open = True  # Открытие диалога
        self.page.update()  # Обновление страницы

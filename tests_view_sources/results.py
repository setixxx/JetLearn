import flet as ft

# Класс ResultsDialog представляет диалоговое окно с результатами теста
class ResultsDialog(ft.AlertDialog):
    def __init__(self, page, correct_answers, total_questions, restart_test, db_manager, app_state, test_number):
        super().__init__()
        # Сохраняем ссылки на необходимые объекты
        self.page = page
        self.test_number = test_number
        self.modal = True
        self.correct_answers = correct_answers
        self.total_questions = total_questions
        self.restart_test = restart_test
        self.db_manager = db_manager
        self.app_state = app_state
        # Задаем заголовок и контент диалога
        self.title = ft.Text("Результаты теста", weight=ft.FontWeight.W_600)
        self.content = TextResults(correct_answers, total_questions)
        # Задаем кнопки действия в диалоге
        self.actions = [
            ft.TextButton(text="Закончить", on_click=self.finish_test),
            ft.FilledButton(text="Начать заново", on_click=self.start_again),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

    # Закрывает диалог
    def close_results(self):
        self.open = False
        self.page.update()

    # Закрывает диалог и переходит на главную страницу
    def finish_test(self, e):
        self.record_results()
        self.close_results()
        self.page.go("/main")

    # Перезапускает тест
    def start_again(self, e):
        self.record_results()
        self.close_results()
        self.restart_test()

    # Сохраняет результаты теста в базе данных
    def record_results(self):
        login = self.app_state.get_login()
        self.db_manager.update_tests(login, self.test_number, self.correct_answers)
        completed_tests = self.db_manager.get_completed_tests_count(login)
        self.app_state.set_completed_tests(completed_tests)


# Класс TextResults представляет контейнер с текстовыми результатами теста
class TextResults(ft.Container):
    def __init__(self, correct_answers, total_questions):
        super().__init__()
        self.height = 70
        self.content = ft.Column(
            [
                ft.Text(f"Отвечено правильно: {correct_answers}/{total_questions}", size=16),
                ft.Text(f"Ваша оценка: {correct_answers * 5 // total_questions}", size=16)
            ]
        )


# Класс Results представляет контейнер с кнопкой для завершения теста и отображения результатов
class Results(ft.Container):
    def __init__(self, page, test_texts, restart_test, db_manager, app_state, test_number):
        super().__init__()
        # Сохраняем ссылки на необходимые объекты
        self.test_number = test_number
        self.page = page
        self.test_texts = test_texts
        self.restart_test = restart_test
        self.db_manager = db_manager
        self.app_state = app_state
        # Задаем стили контейнера
        self.padding = ft.padding.only(top=16, bottom=16)
        self.border_radius = 20
        # Задаем контент контейнера - кнопку "Закончить"
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.FilledButton(text="Закончить", on_click=self.open_test_results)
                    ],
                    spacing=16
                )
            ],
            alignment=ft.MainAxisAlignment.END
        )

    # Открывает диалог с результатами теста
    def open_test_results(self, e):
        correct_answers = sum([test_text.check_answer() for test_text in self.test_texts])
        total_questions = len(self.test_texts)
        # Создаем и открываем диалог
        self.page.dialog = ResultsDialog(self.page,
                                         correct_answers,
                                         total_questions,
                                         self.restart_test,
                                         self.db_manager,
                                         self.app_state,
                                         self.test_number)
        self.page.dialog.open = True
        self.page.update()
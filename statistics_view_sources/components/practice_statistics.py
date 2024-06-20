import flet as ft

# Класс для представления виджета статистики по практике
class PracticeStatistics(ft.Card):
    # Инициализация виджета
    def __init__(self, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Создание столбца с элементами статистики
        self.content = ft.Column(
            [
                # Контейнер для заголовка "Тренажер"
                ft.Container(
                    # Виджет текста заголовка
                    ft.Text(
                        # Текст заголовка
                        "Тренажер",
                        # Размер текста
                        size=20,
                        # Вес шрифта
                        weight=ft.FontWeight.W_500
                    ),
                    # Ширина контейнера
                    width=300,
                    # Высота контейнера
                    height=45,
                    # Отступы слева
                    padding=ft.padding.only(left=32),
                    # Выравнивание по левому нижнему краю
                    alignment=ft.alignment.bottom_left
                ),
                # Контейнер для текста статистики
                ft.Container(
                    # Виджет текста статистики
                    ft.Text(
                        # Формирование текста статистики с использованием данных из состояния приложения
                        f"Правильно отвечено:\n"
                        f"{self.app_state.get_formatted_practice()}",
                        # Размер текста
                        size=16,
                        # Вес шрифта
                        weight=ft.FontWeight.W_400
                    ),
                    # Ширина контейнера
                    width=300,
                    # Высота контейнера
                    height=81,
                    # Отступы
                    padding=ft.padding.only(left=32,
                                            top=16,
                                            bottom=16),
                    # Выравнивание по левому верхнему краю
                    alignment=ft.alignment.top_left
                )
            ],
            # Ширина карточки
            width=300,
            # Высота карточки
            height=126,
            # Междурядный интервал
            spacing=0
        )
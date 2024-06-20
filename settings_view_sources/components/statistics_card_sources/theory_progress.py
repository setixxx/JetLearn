import flet as ft


# Класс для представления виджета прогресса по теории
class TheoryProgress(ft.Container):
    # Инициализация виджета
    def __init__(self, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Установка отступов слева
        self.padding = ft.padding.only(left=22)
        # Установка ширины виджета
        self.width = 344
        # Установка высоты виджета
        self.height = 79
        # Создание строки с элементами прогресса
        self.content = ft.Row(
            [
                # Контейнер для иконки
                ft.Container(
                    # Виджет иконки
                    ft.Icon(
                        # Иконка учебника
                        name=ft.icons.CLASS_OUTLINED,
                        # Цвет иконки
                        color=ft.colors.ON_SURFACE
                    )
                ),
                # Столбец с текстом и полосой прогресса
                ft.Column(
                    [
                        # Виджет текста "Пройденная теория"
                        ft.Text(
                            # Текст
                            "Пройденная теория",
                            # Размер текста
                            size=14,
                            # Вес шрифта
                            weight=ft.FontWeight.W_500
                        ),
                        # Виджет полосы прогресса
                        ft.ProgressBar(
                            # Процент завершения
                            self.app_state.get_completed_theory(),
                            # Ширина полосы прогресса
                            width=214,
                            # Высота полосы прогресса
                            height=4
                        ),
                        # Виджет текста с описанием прогресса
                        ft.Text(
                            # Формирование текста с использованием данных из состояния приложения
                            f"Пройдено "
                            f"{self.app_state.get_formatted_theory()} "
                            f"разделов",
                            # Размер текста
                            size=12,
                            # Вес шрифта
                            weight=ft.FontWeight.W_300
                        )
                    ],
                    # Выравнивание по центру
                    alignment=ft.MainAxisAlignment.CENTER,
                    # Выравнивание по горизонтали
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.START,
            # Выравнивание по вертикали
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
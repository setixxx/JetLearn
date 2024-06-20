import flet as ft


# Класс для представления боковой панели навигации
class NavigationRail(ft.Container):
    # Инициализация панели навигации
    def __init__(self, change_view_callback):
        super().__init__()
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Установка ширины панели
        self.width = 200
        # Установка высоты панели
        self.height = 370
        # Создание виджета боковой панели навигации
        self.content = ft.NavigationRail(
            # Установка индекса выбранного элемента
            selected_index=0,
            # Установка типа отображения подписей
            label_type=ft.NavigationRailLabelType.ALL,
            # Установка высоты панели
            height=364,
            # Установка ширины панели
            width=100,
            # Установка выравнивания элементов
            group_alignment=-1.0,
            # Создание списка пунктов навигации
            destinations=[
                # Первый пункт навигации "Теория"
                ft.NavigationRailDestination(
                    # Иконка неактивного пункта
                    icon=ft.icons.BOOK_OUTLINED,
                    # Иконка активного пункта
                    selected_icon=ft.icons.BOOK,
                    # Содержимое подписи
                    label_content=ft.Text(
                        # Текст подписи
                        "Теория",
                        # Размер текста
                        size=16,
                        # Вес шрифта
                        weight=ft.FontWeight.W_600
                    ),
                ),
                # Второй пункт навигации "Тесты"
                ft.NavigationRailDestination(
                    # Иконка неактивного пункта
                    icon=ft.icons.BROWSE_GALLERY_OUTLINED,
                    # Иконка активного пункта
                    selected_icon=ft.icons.BROWSE_GALLERY,
                    # Содержимое подписи
                    label_content=ft.Text(
                        # Текст подписи
                        "Тесты",
                        # Размер текста
                        size=16,
                        # Вес шрифта
                        weight=ft.FontWeight.W_600
                    )
                ),
                # Третий пункт навигации "Тренажер"
                ft.NavigationRailDestination(
                    # Иконка неактивного пункта
                    icon=ft.icons.VIEW_IN_AR_OUTLINED,
                    # Иконка активного пункта
                    selected_icon=ft.icons.VIEW_IN_AR,
                    # Содержимое подписи
                    label_content=ft.Text(
                        # Текст подписи
                        "Тренажер",
                        # Размер текста
                        size=16,
                        # Вес шрифта
                        weight=ft.FontWeight.W_600
                    )
                )
            ],
            # Обработчик события изменения выбранного элемента
            on_change=change_view_callback
        )
import flet as ft


class LanguageDropDown(ft.Dropdown):
    def __init__(self, change_language, current_language):
        super().__init__()
        self.options = [
            ft.dropdown.Option(text="English", key="en"),
            ft.dropdown.Option(text="Русский", key="ru"),
        ]
        self.border = ft.InputBorder.NONE
        self.text_size = 16
        self.text_style = ft.TextStyle.weight
        self.icon = "LANGUAGE"
        self.value = current_language
        self.width = 200
        self.height = 50
        self.on_change = change_language
        self.border_width = 0
        self.border_radius = 10
        self.padding = ft.padding.only(left=14, right=21)

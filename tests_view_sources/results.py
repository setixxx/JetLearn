import flet as ft

class ResultsDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        self.modal = True,
        self.title = ft.Text("Please confirm"),
        self.content = ft.Text("Do you really want to delete all those "
                               "files?"),
        self.actions = [
            ft.TextButton("Yes", on_click=Results.open_dlg_modal),
            ft.TextButton("No", on_click=Results.close_dlg),
        ],
        self.actions_alignment = ft.MainAxisAlignment.END,
        self.on_dismiss = lambda e: print("Modal dialog dismissed!")

class Results(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(top=16, bottom=16)
        self.border_radius = 20
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.FilledButton(
                            "Закончить",
                        )

                    ],
                    spacing=16
                )
            ],
            alignment=ft.MainAxisAlignment.END
        )

    def open_dlg_modal(self, e):
        self.page.dialog = ResultsDialog()
        ResultsDialog.open = True
        self.page.update()

    def close_dlg(self, e):
        ResultsDialog.open = False
        self.page.update()


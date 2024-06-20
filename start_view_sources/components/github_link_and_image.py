import flet as ft


class GitHubLinkAndImage(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.center_right
        self.width = 200
        self.height = 75
        self.content = ft.ListTile(
            title=ft.Text(
                value="Cоздал setixx",
                size=16,
                weight=ft.FontWeight.W_400,
                max_lines=1,
                text_align=ft.TextAlign.END
            ),
            trailing=ft.Image(
                src=f"assets/github.png",
                height=24,
                width=24,
                fit=ft.ImageFit.COVER,
            ),
            url="https://github.com/setixxx",
            shape=ft.RoundedRectangleBorder(radius=10),
        )

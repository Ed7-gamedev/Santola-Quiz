import flet as ft


class Mainpage:
    def __init__(self):
        pass
    def go_to_quiz(self,page: ft.Page):
        # Navega para a página do quiz
        page.go("/quiz")

    def main_page(self,page: ft.Page):
        page.bgcolor = 'black'
        page.window.width = 450
        page.window.height = 850
        page.vertical_alignment = ft.VerticalAlignment.CENTER

        # Clear views and add new view
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                controls=[
                    ft.Text(value="Olá Mundo", size=30, color='blue'),
                    # Usando a função `go_to_quiz` para navegação
                    ft.ElevatedButton("Ir para o Quiz", on_click=lambda e: go_to_quiz(page))
                ]
            )
        )
    page.update()

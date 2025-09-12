import flet as ft


# se tiver várias views elas elas vão ficar sobrepostas
# se tiver uma home, outra loja e outra carrinho por exemplo elas vão ficar uma por cima da outra
# por isso as views são uma lista
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    def change_route(e):
        match e.control.selected_index:
            case 0:
                page.go("/")
            case 1:
                page.go("/loja")
            case 2:
                page.go("/app")
        # if e.control.selected_index == 0:
        #     page.go('/')
        # elif e.control.selected_index == 1:
        #     page.go("/loja")
        # elif e.control.selected_index == 2:
        #     page.go("app")

    def route_change(route):
        # cada vez que a rota alterar vamos limpar a lista e remover as telas que estão sobrepostas
        page.views.clear()
        # adiciona a view inicial que é a home page
        page.views.append(
            ft.View(
                route="/",
                # serve para quando tiver num app mobile - já que não temos como navegar pelas rotas na parte do www
                appbar=ft.AppBar(
                    title=ft.Text("Meu App"),
                    bgcolor=ft.Colors.BLUE,
                ),
                # elementos que serão renderizados sempre que acessarmos a rota '/'
                controls=[
                    ft.ElevatedButton(
                        text="Ver loja", on_click=lambda _: page.go("/loja")
                    )
                ],
                # habilita a rolagem na página
                scroll=ft.ScrollMode.AUTO,
                bgcolor=ft.Colors.BLACK,
                drawer=ft.NavigationDrawer(
                    controls=[
                        ft.NavigationDrawerDestination(
                            label="home",
                            icon=ft.Icons.HOME,
                        ),
                        ft.NavigationDrawerDestination(
                            label="Loja",
                            icon=ft.Icons.STORE,
                        ),
                        ft.NavigationDrawerDestination(
                            label="App",
                            icon=ft.Icons.PHONE_ANDROID,
                        ),
                    ],
                    on_change=change_route,
                ),
                # tem o mesmo objetivo que o de cima só que ele fica do lado direito da tela
                end_drawer=ft.NavigationDrawer(
                    controls=[
                        ft.NavigationDrawerDestination(
                            label="Configurações",
                            icon=ft.Icons.SETTINGS,
                        ),
                        ft.NavigationDrawerDestination(
                            label="Conta",
                            icon=ft.Icons.VERIFIED_USER,
                        ),
                        ft.NavigationDrawerDestination(
                            label="Sair",
                            icon=ft.Icons.LOGOUT,
                        ),
                    ],
                ),
                # pode ter um botão flutuante apenas em uma página
                floating_action_button=ft.FloatingActionButton(
                    icon=ft.Icons.ADD,
                ),
                # o alinhamento e espaçamento pode ser diferente por página tbm
                horizontal_alignment=ft.CrossAxisAlignment.START,
                vertical_alignment=ft.MainAxisAlignment.START,
                padding=ft.padding.all(20),
            )
        )

        # if page.route == "/store":
        #     page.views.append(
        #         ft.View(
        #             "/loja",
        #             [
        #                 ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.BLUE),
        #                 ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
        #             ],
        #         )
        #     )

        if page.route == "/loja":
            page.views.append(
                ft.View(
                    route="/loja",
                    appbar=ft.AppBar(
                        title=ft.Text("Loja"),
                        bgcolor=ft.Colors.AMBER,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text="Ir para a página inicial",
                            on_click=lambda _: page.go("/"),
                        ),
                        ft.ElevatedButton(
                            text="Ir para App",
                            on_click=lambda _: page.go("/app"),
                        ),
                    ],
                    # serve para um link na app e ele abre a página de  baixo para cima e já tem um botão de fechar - para isso tem que deixar em true
                    fullscreen_dialog=False,
                )
            )

        if page.route == "/app":
            page.views.append(
                ft.View(
                    route="/app",
                    appbar=ft.AppBar(
                        title=ft.Text("App"),
                        bgcolor=ft.Colors.AMBER,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text="Ir para a página inicial",
                            on_click=lambda _: page.go("/"),
                        )
                    ],
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        # tirei para não ficar vermelhinho - mas só funciona com ele
        # page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)

# if __name__ == "__main__":
#     ft.app(target=main, view=ft.AppView.WEB_BROWSER)  - poderia usar assim para rodar numa página web ou usar o -w no terminal

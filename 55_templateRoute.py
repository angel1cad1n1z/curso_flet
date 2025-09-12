import flet as ft


# rotas que podem ser personalizadas
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    def route_change(route):
        # recebe a rota atual
        # verifica essa rota e permitir que peguemos algum parâmetro personalizado
        troute = ft.TemplateRoute(page.route)

        # acessa dentro de loja qualquer produto do catálogo
        if troute.match("/loja/:produto"):
            page.add(
                ft.Text(
                    value=f"Acessando página do produto:{troute.produto}",
                    color=ft.Colors.BLACK,
                )
            )
        elif troute.match("/loja/:produto/pedido/:id"):
            page.add(
                ft.Text(
                    value=f"Acessando página de compra do produto: {troute.produto}, com id: {troute.id}",
                    color=ft.Colors.BLACK,
                )
            )
        else:
            page.add(ft.Text(value="Página não encontrada", color=ft.Colors.BLACK))

    page.on_route_change = route_change
    page.update()


if __name__ == "__main__":
    ft.app(target=main)

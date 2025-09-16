import flet as ft


# pode envolver qualquer componente do flet dentro dele e ele  automaticamente fica seleionável - podendo cliacar e arrastar para remover da página
# muito utilizado em apps mobile - para arquivar ou deletar determinado item
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100
    page.scroll = ft.ScrollMode.AUTO

    def handle_dismiss(e):
        # exclui apenas o componente que realizou a ação de remover - ex: se cliquei no item 5 e arrastei para rememover apenas ele será excluído da lista
        lv.controls.remove(e.control)
        lv.update()

    lv = ft.ListView(
        controls=[
            ft.Dismissible(
                content=ft.Text(value=f"Item {i}", size=40),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                # aparece ao arrastar o item
                background=ft.Container(
                    bgcolor=ft.Colors.BLUE, content=ft.Text(value="Arquivar")
                ),
                secondary_background=ft.Container(
                    bgcolor=ft.Colors.AMBER, content=ft.Text(value="Remover")
                ),
                # pode ser usado para criar a função que vai excluir item definitavente da aplicação
                on_dismiss=handle_dismiss,
                # vai ser disparado apenas quando o componente for atualizado
                on_update= lambda _: print('Atualizado'),
                on_resize= lambda _: print("Redimensionado"),
            )
            for i in range(31)
        ]
    )

    page.add(lv)


if __name__ == "__main__":
    ft.app(target=main)

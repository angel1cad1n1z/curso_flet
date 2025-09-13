import flet as ft


# cria diversos tipos de componentes - janelas de notificaçoes (web) - apps de conversa (mobile)
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100
    # page.scroll = ft.ScrollMode.AUTO

    lt1 = ft.ListTile(
        # pode receber qualquer elemento
        title=ft.Text(value="Título do Primeiro"),
        # pode receber qualquer elemento
        subtitle=ft.Text(value="Subtitulo do primeiro"),
        # recebe qualquer elemento mas é comum usar mais img ou ícone
        leading=ft.Icon(name=ft.Icons.ADB),
        # pode ser um texto, uma badge ou um botão
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Item 01"),
                ft.PopupMenuItem(text="Item 02"),
            ]
        ),
        # espaçamento do conteudo para a aplicação
        content_padding=ft.padding.all(10),
        # mostra que está selecionado
        selected=True,
        on_click=lambda _: print("abriu conversa/notificação"),
        # quando o usuário clicar ele direciona ele para o link
        url="https://google.com.br",
    )

    lt2 = ft.ListTile(
        title=ft.Text(value="Título do segundo"),
        leading=ft.Icon(name=ft.Icons.ADB),
        trailing=ft.Switch(),
        # quando está usando um switch pode habilitar essa 'função' que podemos clicar no nome que ela tbm altera o disposição da bolinha
        toggle_inputs=True,
    )

    page.add(lt1, lt2)  


if __name__ == "__main__":
    ft.app(target=main)

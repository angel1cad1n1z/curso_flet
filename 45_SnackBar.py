import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100
    
    def open_snackBar(e):
        sb.open = True
        page.update()

    # card flutuante
    # utilizado para passar uma informação rápida para o usuário
    sb = ft.SnackBar(
        content= ft.Text(value="Não foi possível processar os dados nesse momento"),
        bgcolor=ft.Colors.RED_400,
        # o usuario pode utilizar para fechar o aviso antes dos 4 segundos
        show_close_icon=True,
        # altera a cor do ícone acima
        close_icon_color=ft.Colors.BLACK,
        padding=ft.padding.all(10),
        # ja vem como padrão a duração de 4 segundos
        duration=4000,
        behavior=ft.SnackBarBehavior.FLOATING,
        # fixed - fica numa posição fixa na tela - pega toda a lateral da app
        # floating - se torna um componente do tipo flutuante - da uma margem da lateral dando uma sensação de que está msm flutuando e tbm tem a opção de clicar e arrastar verticalmente
        margin=ft.margin.all(10),
        # define a direção que o usuario pode clicar e arrastar o snackbar para poder fecha-lo
        dismiss_direction=ft.DismissDirection.START_TO_END,
        # aqui o texto se torna um botão - uma ação
        action= 'Confirmar',
        action_color=ft.Colors.BLUE_GREY_100,
        on_action= lambda _: print('Ação selecionada')
    )
    
    btn1 = ft.ElevatedButton( text="Abrir SnackBar", on_click=open_snackBar)
    
    page.add(btn1, sb)

    
    
if __name__ == "__main__":
    ft.app(target=main)
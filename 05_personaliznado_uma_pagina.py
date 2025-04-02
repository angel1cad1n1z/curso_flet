import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    # por padrão todas as alterações do page é importante que sejam feitas no arquivo principal(main)
    
    # page.window.title_bar_hidden = True #esconde a barra de títulos - dessa forma o título tbm não aparece
    
    # page.window.frameless = True # remove todo e qualquer componente da janela da aplicação
    page.window.bgcolor=  ft.Colors.TRANSPARENT
    page.bgcolor = ft.Colors.TRANSPARENT
        # opções:
            # "white"
            # ft.Colors.white (aqui tem as cores já pré-definidas)
    page.padding = 50 # aplica em  toda a borda o mesmo valor
    # page.padding = ft.padding.all(100)
    # page.padding = ft.padding.only(top= 10, left= 20, right= 20, bottom=10)
    
    page.spacing = 100 #atribui espaçamento entre os elementos da página
    
    page.title = "Primeiros passos no flet" #adiciona um título para a página
    
    txt = ft.Text(
            value= "Olá mundo",
            bgcolor = "amber",
            size = 95
            )
    txt_container = ft.Container(
            ft.Text(
                value = "Bem-Vindo!",
                bgcolor  = "green",
                size = 90
            ),
            alignment=ft.alignment.top_right
                # top_left = Alinha no canto superior esquerdo
                # top_center = Alinha no topo, centralizado
                # top_right = Alinha no canto superior direito
                # center_left = Alinha no centro, à esquerda
                # center = Alinha no centro da tela
                # center_right = Alinha no centro, à direita
                # bottom_left = Alinha no canto inferior esquerdo
                # bottom_center = Alinha no rodapé, centralizado
                # bottom_right = Alinha no canto inferior direito
        )
    
    page.add(txt, txt_container)
    
    page.update()
    
    
ft.app(target= main)
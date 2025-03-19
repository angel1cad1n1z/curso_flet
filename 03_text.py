import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    page.fonts = {
        # a melhor forma de usar fontes é baixando e alocando-as na pasta fonts do assets
        'monteserrat_arq': "fonts/Montserrat-VariableFont_wght.ttf"
    }
    t1 = ft.Text(
        value="Olá, seja bem-vindo Alex!",
        style= ft.TextStyle(size = 50, weight = ft.FontWeight.BOLD),
        # cor do fundo do texto
        # bgcolor= ft.Colors.RED,
        # cor do texto
        color= ft.Colors.BLACK,
        # color = 'black'
        # color = '#FFFFFF'
        font_family= 'monteserrat_arq',
        # italic= True,
        # define a quantidade máxima de linhas do texto. Ainda que o texto quebre ele não ultrpassa o valor passado
        max_lines= 3,
        # define algum caractere que aparece no final para indicar que o texto continua
        # não permite que o texto ultrapasse uma linha ainda que o mesmo quebre
        # no_wrap= True,
        overflow= ft.TextOverflow.ELLIPSIS,
            # CLIP - não mostra nada
            # ELLIPSIS - mostra ...
            # FADE - deixa a ultima parte do texto meio degradê
            
        # permite selecionar o texto. Por default ele vem False.
        selectable= True,
        # sobrescreve o valor anterior de size
        size= 55,
        text_align= ft.TextAlign.CENTER,
        # também está sobrescrevendo o estilo feito antes
        weight= ft.FontWeight.NORMAL,
    )
    
    text_style = ft.TextStyle(
        color= ft.Colors.RED_500, 
        size=70, decoration= ft.TextDecoration.LINE_THROUGH)
    
    title_style = ft.TextStyle(
        # cor do texto
        color= ft.Colors.AMBER,
        # cor de fundo do texto
        bgcolor= ft.Colors.BLACK,
        decoration= ft.TextDecoration.OVERLINE,
            # overline - em cima do texto
            # underline - embaixo do texto
            # LINE_THROUGH - no meio do texto
        # cor do traçado do texto
        decoration_color= ft.Colors.AMBER,
        # peso do traçado do texto, o 1 é o padrão
        decoration_thickness= 2,
        # estilo do traçado do texto
        decoration_style= ft.TextDecorationStyle.WAVY,
            # solid - padrão
            # dashed - traçado
            # dotted - tracinhos mais juntos
            # double - linha mais grossa
            # wavy - traçado em ondas
        )
        
    
    t2 = ft.Text(
        # serve para personalizar partes do texto
        spans= [
            ft.TextSpan(
                text='Texto com link\n', 
                style=ft.TextStyle(
                    color= ft.Colors.BLUE, 
                    weight= ft.FontWeight.NORMAL, 
                    decoration= ft.TextDecoration.UNDERLINE), 
                url= "https://www.google.com/"),
            ft.TextSpan(text='Continuação do texto...\n', style= text_style),
            ft.TextSpan(text='Texto em destaque', style= title_style,)
        ],
        size=50
    )
    
    page.add(t1)    
    page.add(t2)

ft.app(target= main, assets_dir= 'assets')
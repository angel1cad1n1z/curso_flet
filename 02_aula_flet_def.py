import flet as ft

"""
Por convenção criamos uma função main
ela recebe um parâmetro page que possui os detalhes da página
"""
def main(page: ft.Page):
    mensagem = ft.Text(value='Olá mundo!')
    page.add(mensagem)
    
    page.add(ft.Text(value='Meu nome é Lika'))
    
    
    elementos = [
        ft.Text(value="elemento1"),
        ft.Text(value="elemento2"),
        ft.Text(value="elemento3"),
        ft.Text(value="elemento4"),
        ft.Text(value="elemento6"),
    ]
    
    page.add(*elementos)

# o target faz a renderização do app
ft.app(target=main)
import flet as ft

"""
Por convenção criamos uma função main
ela recebe um parâmetro page que possui os detalhes da página
"""
def main(page: ft.Page):
    ...

# o target faz a renderização do app
ft.app(target=main)
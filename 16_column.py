import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    
    col1 = ft.Column(
        controls=[
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="1",
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="2",
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="3",
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="4",
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="5",
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="6",
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="7",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="8",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton(
                # col= {'sm': 4, 'md': 3, 'xl': 2}, # esse componente vai ocupar 4,3 ou 6 das 12 colunas definidas acima dependendo do tamanho da tela
                text="9",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
        ],
        alignment= ft.MainAxisAlignment.CENTER, # para que possamos vizualizar os elementos no centro da página precisamos colocar a coluna num container e assim expandir o container para o espaço vertical disponível na tela e ai sim ver os elementos no centro da página. Sem ser dessa forma não conseguimos vizualizar porque o tamanho da coluna é a quantida total de elementos que ela possui.
        spacing= 20,
        # wrap= True,
        run_spacing= 20,
        width= 100,
        # horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        # horizontal_alignment= ft.CrossAxisAlignment.END,
        # horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
        # horizontal_alignment= ft.CrossAxisAlignment.BASELINE,
        horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
    )
    
    page.add(ft.Container(col1, bgcolor= ft.Colors.RED, expand= True))

ft.app(main)
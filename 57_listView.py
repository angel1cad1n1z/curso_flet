import flet as ft


# permite renderizar vários componentes dentro dele no formato de uma lista
# é feito para renderizar uma grande quantidade de elementos
# semelhante ao gridview
# mais performatico que uma column
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100
    page.scroll = ft.ScrollMode.AUTO
    
    lv = ft.ListView(
        controls=[
            ft.Text(f'Item {i}') for i in range(50)
            ],
        # como podemos receber qualquer componente, ele vai utilizar todo espaçamento e dimensões que o primeiro item utiliza  e vai aplicar esse mesmo espaçamento para todos os itens
        first_item_prototype=False,
        # o listview vai ser exibido na horizontal - vem por defult como false (na vertical)
        horizontal=False,
        # quantos pixels disponiveis por item - é basicamente a distância entre um item e outro - ele bloqueia a quantidade de pixels para um determinado componente
        # item_extent=40,
        # espaçamento das bordas
        padding=ft.padding.all(10),
        # define apenas o espaçamento de um item para o outro - usa esse ou o item_extent
        spacing=10,
        # define quantos pixels tem o divisor entre os itens - por padrão vem como None/0 - pelo que vi só funciona com o spacing
        divider_thickness=1,
    )
    
    page.add(lv)

if __name__ == "__main__":
    ft.app(target=main)
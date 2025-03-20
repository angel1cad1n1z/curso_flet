import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    img = ft.Image(
        src=f"images/10353_8A5CCF09AC979AF1.webp",
        border_radius= ft.border_radius.all(20),
            # vertical - top(bordas superiores) e bottom(bordas inferiores)
            # only - persobaliza as bordas individualmente
                # top_left= 25,
                # top_right= 150,
                # bottom_left= 50,
                # bottom_right=100)
            # horizontal - left(esquerda) e right(direita)
            # all - todas as bordas ficam com um valor fixo
        # largura
        width= 1000,
        # altura
        height= 500,
        fit= ft.ImageFit.CONTAIN,
            # fit_height - preenche a altura
            # FIT_WIDTH - preenche a largura
            # contain - não muda a proporção da imagem , ela vai caber dentro da menor dimensão possível
            # cover - preenche todo o espaço disponível que foi definido no width e no height
        repeat= ft.ImageRepeat.REPEAT,
        tooltip='Telescópio Hubble captura imagem nítida do verão em Saturno',
    )
    
    img2 = ft.Image(
        src=f"images/img2.jpg",
        # o texto aparece quando passa o mause em cima da imagem
        tooltip="Planeta Saturno",
        border_radius=ft.border_radius.only(
                top_left= 2000,
                top_right= 500,
                bottom_left= 500,
                bottom_right=1000))

    page.add(img, img2)

ft.app(target= main, assets_dir= 'assets')